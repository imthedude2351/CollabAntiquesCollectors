from django.db import models
from django.urls import reverse
# Create your models here.
class Subscriber(models.Model):
    full_name= models.CharField(max_length=100)
    email= models.EmailField()
    def __str__(self):
        return f"{self.full_name}, {self.email}"
    def get_absolute_url(self):
        return reverse('confirmation')