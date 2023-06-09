from django.urls import path

from . import views

app_name = "login_signup_authentication"
urlpatterns = [
    path("", views.login_user, name="index"),
]