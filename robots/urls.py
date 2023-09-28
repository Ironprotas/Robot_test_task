
from django.urls import path
from .views import create_robot, get_robot

urlpatterns = [
    path('api/create_robot/', create_robot, name='create-robot'),
    path('api/get_robot/<str:model>/', get_robot, name="get-robot")

]