from django.urls import path
from rest_framework.authtoken import views

from .views import UserCreate, LoginView


urlpatterns = [
    path("user/create/", UserCreate.as_view(), name="user_create"),
    path("user/login/", LoginView.as_view(), name="user_login"),
    # path("user/login/", views.obtain_auth_token, name="login"),
]
