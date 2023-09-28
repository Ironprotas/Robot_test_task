from django.urls import path
from .views import export_excel

urlpatterns = [
    path('export/', export_excel, name='export')
]
