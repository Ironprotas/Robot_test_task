from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Robot, Customer, RobotRequest, RobotAvailability
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)


@csrf_exempt
def add_email(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            if not email:
                return JsonResponse({'error': 'Email is required'}, status=400)

            customer, created = Customer.objects.get_or_create(email=email)
            if created:
                return JsonResponse({'message': 'Email added successfully'}, status=201)
            else:
                return JsonResponse({'message': 'Email already exists'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)



@csrf_exempt
def send_email(request):
    logger.info(f"Received request: {request.method} {request.path}")
    if request.method == 'POST':
        try:
            data = request.POST  # В POST запросе мы ожидаем получить данные в теле запроса

            model = data.get('model')
            version = data.get('version')
            customer_email = data.get('customer')

            if Customer.objects.filter(email=customer_email).exists():
                customer = Customer.objects.get(email=customer_email)
            else:
                return JsonResponse({'Error': 'Email not found'}, status=404)

            try:
                robot = Robot.objects.filter(model=model, version=version).first()

                if robot:
                    if RobotAvailability.available:
                        subject = 'Робот доступен'
                        message = f'Добрый день!\n Вы интересовались нашим роботом модели {model}, версии {version}.\n'
                        from_email = [customer_email]
                        recipient_list = [customer_email]

                        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

                        return JsonResponse({'message': 'Robot available and notification sent'}, status=200) # отправка успешна
                    else:
                        return JsonResponse({'Error': "test"}, status=400)
                else:
                    RobotRequest.objects.create(
                        customer=Customer.objects.get(email=customer_email),
                        model=model,
                        version=version)
                    return JsonResponse({'message': 'You robot add in queue'}, status=200)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)




