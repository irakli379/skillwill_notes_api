from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):
    user = models.ForeignKey(User, related_name='note', on_delete=models.CASCADE)
    header = models.CharField(max_length=150)
    text = models.TextField(max_length=555)
