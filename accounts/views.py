from django.shortcuts import redirect, render
from django.contrib import auth, messages
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if request.method == 'POST':
        print(request.POST)
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email taken')
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name)
                    user.save()
                    return redirect('login')
        else:
            messages.error(request,'Password Mismatch')
            return redirect('register')



        
    return render(request,'accounts/register.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password1']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.error(request,"Invalid Credentials")
    return render(request,'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')