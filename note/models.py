from django.db import models
from django.utils import timezone

# Create your models here.
class notes(models.Model):
  title = models.CharField(max_length=200)
  note_date = models.DateTimeField(default=timezone.now() ,null=True)
  notes = models.TextField()

  def __str__(self):
    return self.title

class extra(models.Model):
  heading = models.CharField(max_length=100)
  para = models.TextField()

  def __str__(self):
    return self.heading
    
