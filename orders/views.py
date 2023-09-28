from django.shortcuts import render
from django.http import  HttpResponse
import csv
from robots.models import Robot
def export_post_csv(request):



    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = "attachment; filename=Robots.csv"
    writer = csv.writer(response)

    writer.writerow(['Модель','Версия','Количество за неделю'])
    posts = Robot.objects.all().values_list('model','version','quantity')
    for post in posts:
        writer.writerow(post)
    return response

