from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class task(models.Model):
    objects = None
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    id = models.AutoField(primary_key=True)
    task = models.CharField(max_length=200)
    desc = models.TextField()
    created = models.DateTimeField(auto_now=True, null=True)
    updated = models.DateTimeField(auto_now_add=True, null=True)

    # class Meta:
    #     ordering = ['-updated', '-created']

    def __str__(self):
        return self.task
