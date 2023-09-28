from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Robot, RobotAvailability, Customer

@csrf_exempt
def check_robot_availability(request):
    if request.method == 'GET':
        model = request.GET.get('model')
        version = request.GET.get('version')

        try:
            robot = Robot.objects.get(model=model, version=version)

            queued_notifications = RobotAvailability.objects.filter(robot=robot, queued_for_notification=True)
            for notification in queued_notifications:
                notification.queued_for_notification = False
                notification.save()
                notification.notify_customer()

            return JsonResponse({'message': 'Robot available'}, status=200)

        except Robot.DoesNotExist:
            customer_email = request.GET.get('customer')
            customer, created = Customer.objects.get_or_create(email=customer_email)
            robot_availability = RobotAvailability(robot=None, available=False, queued_for_notification=True,
                                                   customer=customer)
            robot_availability.save()

            return JsonResponse({'message': 'Robot not available, notification queued'}, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

