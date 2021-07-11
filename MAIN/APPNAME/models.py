from django.db import models
from django.contrib.auth.models import User

class Password(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    logo = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
    