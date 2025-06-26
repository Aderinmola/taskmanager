from django.urls import path
from .views import PostListCreateView, PostDetailView

app_name = 'post'


urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
