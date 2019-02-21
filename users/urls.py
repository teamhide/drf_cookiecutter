from django.urls import path
from users.views.v1 import User, UserList


urlpatterns = [
    path('v1/users/', UserList.as_view()),
    path('v1/users/<int:no>', User.as_view())
]
