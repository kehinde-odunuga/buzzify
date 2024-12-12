from django.urls import path
from buzzer.views import RegisterUserView

urlpatterns = [
    path('api/register/', RegisterUserView.as_view(), name='register'),
]