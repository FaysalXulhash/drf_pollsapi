from django.urls import path
from .views import UserCreateApi, LoginApi

urlpatterns = [
    path('user/create/', UserCreateApi.as_view(), name='create-user'),
    path('user/login/', LoginApi.as_view(), name='login'),
]