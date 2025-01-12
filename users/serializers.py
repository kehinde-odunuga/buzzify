from rest_framework import serializers
from django.contrib.auth import get_user_model
from users.models import UserFollow, Message

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'password', 'bio', 'profile_picture',
                 'cover_photo', 'website', 'location', 'followers_count',
                 'following_count')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }

    def get_followers_count(self, obj):
        return obj.followers.count()

    def get_following_count(self, obj):
        return obj.following.count()

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'sender', 'recipient', 'content', 'created_at', 'is_read')
        read_only_fields = ('sender', 'is_read')