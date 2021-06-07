from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login as loginuser,logout
from django.contrib.auth.decorators import login_required
from quiz.models import Question
from quiz.models import Course
# Create your views here.

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login as loginuser,logout
from django.contrib.auth.decorators import login_required
from quiz.models import students
# Create your views here.
@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        q=Course.objects.all()
        return render(request , 'course.html' , context={'questions' : q})
def home1(request,pk):
    if request.user.is_authenticated:
        q=Course.objects.get(id=pk)
        question=Question.objects.all().filter(course=q)

        print(q)
        print(question)
        print("hiiiiiiiiii")
        return render(request , 'quiz.html' , context={'questions' : question})
def login(request):
    if request.method == 'POST':
        print("hi")
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print("done",user)
            if user is not None:
                loginuser(request,user)
                return redirect('home')
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
def signup(request):
    if request.method=='POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
def signout(request):
    logout(request)
    return redirect('home')

'''
@login_required('login')
def home(request):
    return HttpResponse("hi")
def login(request):
    if request.method == 'POST':
        print("hi")
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print("done",user)
            if user is not None:
                loginuser(request,user)
                return redirect('home')
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
def signup(request):
    if request.method=='POST':
        form = StudentUserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
def signout(request):
    logout(request)
    return redirect('home')





''''''
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import User

def index(request):
    return render(request, 'index.html')

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')

    hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=hashed_password, email=request.POST['email'])
    user.save()
    request.session['id'] = user.id
    return redirect('/success')

def login(request):
    if (User.objects.filter(email=request.POST['login_email']).exists()):
        user = User.objects.filter(email=request.POST['login_email'])[0]
        if (bcrypt.checkpw(request.POST['login_password'].encode(), user.password.encode())):
            request.session['id'] = user.id
            return redirect('/success')
    return redirect('/')

def success(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return HttpResponse("hi")
    #return render(request, 'login.html', context)
'''
