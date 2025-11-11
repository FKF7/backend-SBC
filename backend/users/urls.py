from django.urls import path
from .views import login_and_set_cookies

urlpatterns = [
    path("login/", login_and_set_cookies, name="login"),
]
