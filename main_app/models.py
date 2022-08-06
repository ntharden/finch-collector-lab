from django.db import models

class Friend(models.Model):
  name = models.CharField(max_length=100)
  job = models.CharField(max_length=50)
  description = models.TextField(max_length=250)
  def __str__(self):
    return self.name