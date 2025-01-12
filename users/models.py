from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.conf import settings

class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    cover_photo = models.ImageField(upload_to='cover_photos/', blank=True)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    following = models.ManyToManyField(
        'self',
        through='UserFollow',
        symmetrical=False,
        related_name='followers'
    )

    def __str__(self):
        return self.username

class UserFollow(models.Model):
    follower = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following_relationships'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower_relationships'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def clean(self):
        if self.follower == self.following:
            raise ValidationError("Users cannot follow themselves.")

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)