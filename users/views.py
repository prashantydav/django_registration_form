from django.shortcuts import render , redirect , reverse
from django.contrib.auth.models import User
from django.contrib.auth import login , logout , authenticate
from .forms import (
    UserForm , 
    AuthForm ,
)
from registrationform.mixins import FormErrors
from django.contrib import messages

def home_view(request):
    return render(request , 'home.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            messages.success(request , 'account successfully created!!')
            return redirect('../signin/')
        else:
            message = FormErrors(form)
            messages.error(request, message)
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})

# def signin_view(request):
#     print("0")
#     if request.method == 'POST':
#         form = AuthForm(request.POST)
#         print("1")
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             print("2")
#             user = authenticate(request , username=username, password=password)

#             if user is not None:
#                 login(request , user)
#                 print("3")
#                 messages.success(request , "you are logged in!!")
#                 return redirect("users:home")
        
#         else:
#             print('wht the fuk is gn on')
#             message = FormErrors(form)
#             messages.error(request , message)
#             print(message)
    
#     form = AuthForm()
#     print("5")
#     return render(request, 'login.html' ,{
#         'form' :form
#     })

def signin_view(request):
    if request.method == "POST":
        form = AuthForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("users:home")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthForm()
    return render(request=request, template_name="login.html", context={"form":form})

def logout_view(request):
    logout(request)
    return redirect('users:signin')


