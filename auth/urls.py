from django.urls import path
from auth.views.v1 import Auth


urlpatterns = [
    path('', Auth.as_view()),
]
