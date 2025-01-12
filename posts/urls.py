from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from rest_framework_nested import routers
from posts.views import PostViewSet, CommentViewSet, NotificationViewSet

# Main router for posts and notifications
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'notifications', NotificationViewSet, basename='notification')

# Nested router for comments
posts_router = routers.NestedDefaultRouter(router, r'posts', lookup='post')
posts_router.register(r'comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(posts_router.urls)),
    # Custom post actions
    path('posts/<uuid:pk>/like/', PostViewSet.as_view({'post': 'like'}), name='post-like'),
    path('posts/<uuid:pk>/unlike/', PostViewSet.as_view({'post': 'unlike'}), name='post-unlike'),
    path('posts/<uuid:pk>/repost/', PostViewSet.as_view({'post': 'repost'}), name='post-repost'),
    # Feed endpoints
    path('feed/', PostViewSet.as_view({'get': 'feed'}), name='user-feed'),
    path('trending/', PostViewSet.as_view({'get': 'trending'}), name='trending-posts'),
    # Notification actions
    path('notifications/mark-all-read/', 
         NotificationViewSet.as_view({'post': 'mark_all_read'}), 
         name='mark-all-notifications-read'),
]