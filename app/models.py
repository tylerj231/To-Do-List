from django.contrib.auth.models import AbstractUser
from django.db import models


class Task(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True)
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", blank=True)

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.TextField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
