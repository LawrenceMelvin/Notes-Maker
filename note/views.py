from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import notes
from django.http import HttpResponse
from .forms import notesupdate,NewUserForm
from django.contrib.auth.forms import AuthenticationForm 
# Create your views here.
def register(request):
  form = NewUserForm()
  if request.method == 'POST':
      form = NewUserForm(request.POST)
      if form.is_valid:
        user = form.save()
        login(request,user)
        messages.success(request,"Registration sucessful")
        return redirect('home')
  else:
    form = NewUserForm()
  context={'form':form}
  return render(request,'note/register.html',context)

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('home')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="note/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('login')

@login_required(login_url='login')
def index(request):
  context ={'notes':notes.objects.all()}
  return render(request,'note/home.html',context)

def add(request):
  form = notesupdate()
  if(request.method=='POST'):
    form = notesupdate(request.POST,)
    if form.is_valid():
      form.save()
      messages.success(request,'Notes succesfully created')
      return redirect('home')
  else:
    form = notesupdate()
  context = {'form':form}
  return render(request,'note/add.html',context)

def delete(request,note_id):
  if request.method == 'POST':
    print(request.POST)
    ele = notes.objects.get(id=note_id)
    ele.delete()
    messages.info(request,"Notes Removed")
    return redirect('home')
