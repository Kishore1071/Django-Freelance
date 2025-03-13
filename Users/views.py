from django.shortcuts import render, redirect
from .models import *

def UserList(request):

    all_user = User.objects.all()

    context = {
        'title': 'User List',
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

def UpdateUser(request, id):

    user = User.objects.get(id=id)

    context = {
        'user': user
    }

    if request.method == "POST":

        user_check = User.objects.filter(username = request.POST['username']).exclude(id=id)

        if len(user_check) > 0:

            context = {
                "error": "Username already exists!"
            }
            
            return render(request, 'signup.html', context)
        else:

            user_update = User.objects.filter(username = request.POST['username'])

            user_update.update(username = request.POST['username'], email = request.POST['user_email'], phone_number = request.POST['phone_number'], first_name = request.POST['first_name'], last_name = request.POST['last_name'])

            return redirect('/user/list/')

    return render(request, 'users/user_update.html', context)

def DeleteUser(request, id):

    user = User.objects.get(id=id)

    user.delete()

    return redirect('/user/list/')






