<<<<<<< HEAD
import openpyxl
from django.db.models import Sum
from robots.models import Robot
from django.http import HttpResponse
from datetime import datetime, timedelta

def export_excel(request):
    wb = openpyxl.Workbook()

    today = datetime.now()
    week_ago = today - timedelta(weeks=1)

    # Получите данные с группировкой по модели и версии, а также суммой количества
    robots = Robot.objects.filter(created__gte=week_ago).values('model', 'version').annotate(
        total=Sum('quantity')
    )

    sheet = wb.active
    sheet.title = "Robots Data"

    sheet.append(['Модель', 'Версия', 'Количество за неделю'])

    for robot in robots:
        model = robot['model']
        version = robot['version']
        total = robot['total']
        sheet.append([model, version, total])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=robots.xlsx'

    wb.save(response)

    return response
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> 366629b (First task done)
