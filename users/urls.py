from django.urls import path
from .views import CustomUserCreate, GetCurrentUser


app_name = 'users'

urlpatterns = [
    path('register/', CustomUserCreate.as_view(), name='create_user'),
    path('profile/', GetCurrentUser.as_view(), name='current_user',)
]


