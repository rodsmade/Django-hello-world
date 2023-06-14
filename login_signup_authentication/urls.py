from django.urls import path

from . import views

app_name = "login_signup_authentication"
urlpatterns = [
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
]