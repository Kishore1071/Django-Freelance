from django.shortcuts import render, redirect
from .models import *
from .forms import *

def CategoryAdd(request):


    data = {
        "category_form": CategoryForm()
    }

    if request.method == 'POST':

        print(request.POST['category_name'])

        new_category = Category(category_name = request.POST['category_name'], description = request.POST['description'])

        new_category.save()

        return redirect('/inventory/category/list/')

    return render(request, 'category/category_add.html', data)

def CategoryList(request):

    context = {
        "all_category": Category.objects.all()
    }

    return render(request, 'category/category_list.html', context)

def CategoryUpdate(request, id):

    selected_category = Category.objects.get(id = id)

    data = {
        "category_form": CategoryForm(instance=selected_category)
    }

    if request.method == 'POST':

        update_category = Category.objects.filter(id = id)

        update_category.update(category_name = request.POST['category_name'], description = request.POST['description'])

        return redirect('/inventory/category/list/')


    return render(request, 'category/category_add.html', data)

def DeleteCategory(request, id):

    selected_category = Category.objects.get(id = id)

    selected_category.delete()

    return redirect('/inventory/category/list/')


