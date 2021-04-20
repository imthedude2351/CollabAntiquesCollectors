from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import Subscriber


def home(request):
    return render(request, 'base.html')


class SubscriberCreate(CreateView):
  model = Subscriber
  fields = '__all__'
  
def dashboard(request):
  subs = Subscriber.objects.all()
  return render(request, 'dashboard.html', {'subs' : subs})
  
def confirmation(request):
  return render(request, 'confirmation.html')