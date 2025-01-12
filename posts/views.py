
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.db.models import Count
from datetime import timedelta
from django.utils import timezone
from posts.models import Post, Comment, Notification
from posts.serializers import PostSerializer, CommentSerializer, NotificationSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly
from rest_framework import viewsets, permissions, filters, status
from .perm import IsAuthorOrReadOnly


class PostPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = PostPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['content', 'tags__name']

    def get_queryset(self):
        queryset = Post.objects.all()
        if self.action == 'feed':
            following = self.request.user.following.all()
            queryset = queryset.filter(author__in=following)
        elif self.action == 'trending':
            last_24h = timezone.now() - timedelta(hours=24)
            queryset = queryset.filter(created_at__gte=last_24h)\
                              .annotate(engagement=Count('likes') + Count('comments'))\
                              .order_by('-engagement')
        return queryset

    def perform_create(self, serializer):
        # Assign the authenticated user as the author of the post
        serializer.save(author=self.request.user)
        
    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        post = self.get_object()
        post.likes.add(request.user)
        Notification.objects.create(
            recipient=post.author,
            sender=request.user,
            notification_type='like',
            post=post
        )
        return Response({"status": "liked"})

    @action(detail=True, methods=['POST'])
    def unlike(self, request, pk=None):
        post = self.get_object()
        post.likes.remove(request.user)
        return Response({"status": "unliked"})

    @action(detail=True, methods=['POST'])
    def repost(self, request, pk=None):
        original_post = self.get_object()
        repost = Post.objects.create(
            author=request.user,
            content=original_post.content,
            is_repost=True,
            original_post=original_post
        )
        return Response(PostSerializer(repost).data)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_pk'])

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.kwargs['post_pk'])
        serializer.save(author=self.request.user, post=post)

class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)\
                                 .order_by('-created_at')

    @action(detail=False, methods=['POST'])
    def mark_all_read(self, request):
        self.get_queryset().update(is_read=True)
        return Response({"status": "marked all as read"})