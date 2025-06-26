from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied

from .models import Post
from .serializers import PostSerializer

# from django.contrib.auth.models import User
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AuthorSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

# User = settings.AUTH_USER_MODEL

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Automatically set the author


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if self.request.user != self.get_object().author:
            raise PermissionDenied("You do not have permission to edit this post.")
        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user != instance.author:
            raise PermissionDenied("You do not have permission to delete this post.")
        instance.delete()


class AuthorListView(APIView):
    def get(self, request):
        authors = User.objects.filter(posts__isnull=False).distinct()
        # authors = User.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

