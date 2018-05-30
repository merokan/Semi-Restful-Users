from django.shortcuts import render, redirect 
from models import *

def index(request):
    context = {
        'user_data' : User.objects.all()
    }
    return render(request, "users/index.html", context)

def new(request):
    return render(request, "users/new.html")

def edit(request, user_id):
    context = {
        'id' : user_id
    }
    return render(request, "users/edit.html", context)

def show(request, user_id):
    context = {
        'id': user_id,
        'first_name': User.objects.get(id=user_id).first_name,
        'last_name' : User.objects.get(id=user_id).last_name,
        'email' : User.objects.get(id=user_id).email,
        'created_at' : User.objects.get(id=user_id).created_at
    }
    return render(request, "users/show.html", context)

def create(request):
    if request.method == "POST":
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
        return redirect("/users/"+str(user.id))
    else:
        return redirect('/users')

def destroy(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect("/users")

def update(request, user_id):
    if request.method == "POST":
        update = User.objects.get(id=user_id)
        update.first_name = request.POST['first_name']
        update.last_name = request.POST['last_name']
        update.email = request.POST['email']
        update.save()
        return redirect("/users/"+str(user_id))
    else:
        return redirect('/users')
    
