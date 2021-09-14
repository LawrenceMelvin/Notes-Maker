from django.shortcuts import render,redirect
from django.contrib import messages
from .models import notes
from django.http import HttpResponse
from .forms import notesupdateform
# Create your views here.
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
      messages.success(request,f'Notes succesfully created')
      return redirect('home')
  else:
    form = notesupdateform()
  context = {'form':form}
  return render(request,'note/add.html',context)
