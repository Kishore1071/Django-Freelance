from django.urls import path
from .views import *

urlpatterns = [
    path('list/', UserList),
    path('create/', CreateUser)
]