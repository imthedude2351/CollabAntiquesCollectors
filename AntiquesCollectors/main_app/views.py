from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Subscriber

def subscriber_index(request):
  subscribers = Subscriber.objects.all()
  return render(request, 'subscribers/base.html', { 'subscribers': subscribers })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'base.html', context)

def home(request):
    return render(request, 'base.html')

class SubscriberCreate(CreateView):
  model = Subscriber
  fields = '__all__'

def dashboard(request):
  subs = Subscriber.objects.all()

  return render(request, 'dashboard.html', {
    'subs' : subs,
     })

