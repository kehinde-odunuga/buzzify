from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import AuthViewSet, UserViewSet, MessageViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include([
        path('register/', AuthViewSet.as_view({'post': 'register'}), name='register'),
        path('login/', AuthViewSet.as_view({'post': 'login'}), name='login'),
    ])),
]