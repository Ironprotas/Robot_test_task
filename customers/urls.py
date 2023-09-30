from django.urls import path
from .views import send_email, add_email

urlpatterns = [
    path('send_email/', send_email, name='send-email'),
    path('add_email/', add_email, name='add-email'),
]