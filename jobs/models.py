from django.db import models
Class Job(models.Model):
image=models.ImageField('image/')
summary=models.CharField(max_length=200)
