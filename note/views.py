from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .models import notes
from django.http import HttpResponse
from .forms import notesupdateform,createuserform
# Create your views here.
def registration(request):
  form = createuserform()
  if request.method == 'POST':
    form = createuserform(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request,'Account is created ')
      return redirect('login')
  else:
    form = createuserform()
  context={'form':form}
  return render(request,'note/register.html',context)

def loginpage(request):
  if request.method == 'POST':
    username=request.POST.get('username')
    password=request.POST.get('password')
    print(username)
    print(password)
    user = authenticate(request,username=username,password=password)
    if user is not None:
      login(request,user)
      return redirect('home') 
    else:
      messages.info(request,'Username or Password incorrect')
  context={}
  return render(request,'note/login.html',context)

def logoutview(request):
  logout(request)
  return redirect('login')

def index(request):
  context ={'notes':notes.objects.all(),}
  return render(request,'note/home.html',context)

def add(request):
  form = notesupdateform()
  if request.method == 'POST':
    print(request.POST)
  if(request.method=='POST'):
    form = notesupdateform(request.POST,)
    if form.is_valid():
      form.save()
      messages.success(request,'Notes succesfully created')
      return redirect('home')
  else:
    form = notesupdateform()
  context = {'form':form}
  return render(request,'note/add.html',context)

def delete(request,note_id):
  if request.method == 'POST':
    ele = notes.objects.get(id=note_id)
    ele.delete()
    messages.info(request,"Notes Removed")
    return redirect('home')