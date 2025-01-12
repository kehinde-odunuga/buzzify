from rest_framework import serializers
from posts.models import Post, Comment, Hashtag, Notification
from users.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'author', 'content', 'created_at', 'likes_count')

    def get_likes_count(self, obj):
        return obj.likes.count()

class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ('id', 'name', 'created_at')

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    reposts_count = serializers.SerializerMethodField()
    tags = HashtagSerializer(many=True, read_only=True)
    mentioned_users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'content', 'media', 'created_at', 'updated_at',
                 'likes_count', 'comments', 'comments_count', 'tags',
                 'mentioned_users', 'is_repost', 'original_post', 'reposts_count')

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_comments_count(self, obj):
        return obj.comments.count()

    def get_reposts_count(self, obj):
        return obj.reposts.count()

class NotificationSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    
    class Meta:
        model = Notification
        fields = ('id', 'recipient', 'sender', 'notification_type', 'post',
                 'comment', 'created_at', 'is_read')