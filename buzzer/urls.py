from django.urls import path
from buzzer.views import RegisterUserView, LoginUserView

urlpatterns = [
    path('api/register/', RegisterUserView.as_view(), name='register'),
    path('api/login/', LoginUserView.as_view(), name='login'),
]