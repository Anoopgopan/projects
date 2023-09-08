from django.shortcuts import render
from . forms import UserRegistrationForm
# Create your views here.
from . models import UserRegistration
from django.contrib.auth.models import User




def loginform(request):
    return render(request, 'loginform.html')


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    if username == 'admin@gmail.com':
        registered_users = UserRegistration.objects.all()
    else:
        registered_users = UserRegistration.objects.filter(username=username)
    print("Registered users ::::::::::::::::: ",registered_users)
    if registered_users:
        for user in registered_users:
            print("::::::::::::::::: ",user)
            if user and user.password == password:
                return render(request, 'registered_users.html',{"registered_users":registered_users})
            else:
                return render(request, "loginfail.html")
    else:
            return render(request, "loginfail.html")
        

def signupform(request):
    return render (request,'signupform.html')


def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'successfulsignup.html')
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form':form})




def update(request, username):
    try:
        user = UserRegistration.objects.get(username=username)
        if request.method == "POST":
            password = request.POST['password']
        print("user : ", password)
    except User.DoesNotExist:
        print("USERNAME DOES NOT EXIST")

    user.password=password
    user.save()
    
    # if updated:
    #     registered_users = UserRegistration.objects.filter(username=username)
    #     for user in registered_users:
    registered_users = UserRegistration.objects.filter(username=username)
    return render(request, 'registered_users.html', {'registered_users':registered_users})