from django.urls import path
from .views import PostListCreateView, PostDetailView, AuthorListView

app_name = 'post'


urlpatterns = [
]



urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('authors/', AuthorListView.as_view(), name='author-list'),    
]
