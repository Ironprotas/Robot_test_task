from django.urls import path
from .views import export_post_csv

urlpatterns = [
    path('export/', export_post_csv, name='export')
]
