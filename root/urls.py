from django.urls import path, include
from root.views import Register


urlpatterns = [
    path("register/", Register.as_view()),
    path("", include("rest_framework.urls"))
]
