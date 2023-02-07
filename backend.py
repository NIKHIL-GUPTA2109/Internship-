from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    user_instance = models.ForeignKey(User, on_delete=models.CASCADE)

class Artist(models.Model):
    name = models.CharField(max_length=100)
    work = models.ManyToManyField(Work)

class Work(models.Model):
    WORK_TYPE_CHOICES = [
        ('Youtube', 'Youtube'),
        ('Instagram', 'Instagram'),
        ('Other', 'Other'),
    ]

    link = models.URLField()
    work_type = models.CharField(max_length=20, choices=WORK_TYPE_CHOICES)

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_client(sender, instance, created, **kwargs):
    if created:
        Client.objects.create(user_instance=instance)

