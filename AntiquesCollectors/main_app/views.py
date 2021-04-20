from django.shortcuts import render
from django.http import HttpResponse
from .models import Subscriber

def index(request):
    submitbutton= request.POST.get("submit")
    fullname=''
    emailvalue=''
    form= UserForm(request.POST or None)
    if form.is_valid():
        fullname= form.cleaned_data.get("fullname"),
        emailvalue= form.cleaned_data.get("email")
    context= {'form': form, 'fullname': fullname,
              'submitbutton': submitbutton, 'emailvalue':emailvalue}
    return render(request, 'base.html', context)

def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')