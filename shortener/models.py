from django.db import models

# Create your models here.

class Url(models.Model):
  url=models.CharField(max_length=99999)
  uuid= models.CharField(max_length=10)

  def __str__(self):
    return self.id