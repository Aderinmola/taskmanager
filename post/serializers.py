from rest_framework import serializers
from .models import Post

from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


# from django.contrib.auth.models import User

# User = settings.AUTH_USER_MODEL

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  # Show username

    class Meta:
        model = Post
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    post_count = serializers.IntegerField(source='posts.count', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'post_count']

