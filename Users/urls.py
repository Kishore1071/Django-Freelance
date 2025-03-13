from django.urls import path
from .views import *

urlpatterns = [
    path('list/', UserList),
    path('create/', CreateUser),
    path('update/<int:id>/', UpdateUser, name='update_user'),
    path('delete/<int:id>/', DeleteUser, name='delete_user'),
]