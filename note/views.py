from django.shortcuts import render,redirect
from django.contrib import messages
from .models import notes
from django.http import HttpResponse
from .forms import notesupdateform
# Create your views here.
def index(request):
  context ={'notes':notes.objects.all()}
  return render(request,'note/home.html',context)

def add(request):
  if(request.method=='POST'):
    form = notesupdateform(request.POST,instance=request.note.notes)
    if form.is_valid():
      form.save()
      messages.success(request,f'Notes succesfully created')
      return redirect('home')
  else:
    form = notesupdateform()
  return render(request,'note/add.html')
