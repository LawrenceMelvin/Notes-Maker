from django.db import models

# Create your models here.
class notes(models.Model):
  title = models.CharField(max_length=200)
  note_date = models.DateTimeField('notes date')
  notes = models.TextField()

  def __str__(self):
    return self.title
