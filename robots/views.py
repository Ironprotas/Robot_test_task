from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Robot
import json

@csrf_exempt
def create_robot(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        #    serial = data.get('serial')
            model = data.get('model')
            version = data.get('version')
            created = data.get('created')

            existing_robot= Robot.objects.filter(
           #     serial = serial,
                model = model,
                version = version,
                created = created
            ).first()

            if existing_robot:
                return HttpResponse("Error: Robot with paramert exists", status=400, )

            robot = Robot.objects.create(
            #    serial=serial,
                model=model,
                version=version,
                created=created
            )

            return JsonResponse({'message': 'Robot added'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    elif request.method == 'GET':
        return JsonResponse({'message': 'GET request handled'}, status=200)
    return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def get_robot(request, model):
    if request.method == 'GET':
        try:
            robots = Robot.objects.filter(model=model)
            if not robots:
                return HttpResponse("Error: Robots not found", status=404)

            data = []
            for robot in robots:
                data.append({
                  #  "serial": robot.serial,
                    "model": robot.model,
                    "version": robot.version,
                    "created": robot.created
                })

            return JsonResponse(data, status=200, safe=False)
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}", status=500)
    return HttpResponse("Error: Method not allowed", status=405)
