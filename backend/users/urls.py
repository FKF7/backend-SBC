from django.urls import path
from .views import login_and_set_cookies, me

urlpatterns = [
    path("login/", login_and_set_cookies, name="login"),
    path("me/", me, name="me")
]
