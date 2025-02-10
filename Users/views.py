from django.shortcuts import render, redirect
from .models import *

def UserList(request):

    all_user = User.objects.all()

    context = {
        'all_user': all_user
    }

    return render(request, 'users/user_list.html', context)

def CreateUser(request):

    if request.method == "POST":

        user_check = User.objects.filter(username = request.POST['username'])

        if len(user_check) > 0:

            context = {
                "error": "Username already exists!"
            }
            
            return render(request, 'signup.html', context)
        else:

            new_user = User(username = request.POST['username'], email = request.POST['user_email'], phone_number = request.POST['phone_number'])

            new_user.set_password(request.POST['user_password'])

            new_user.save()

            return redirect('/user/list/')

    return render(request, 'users/user_add.html')