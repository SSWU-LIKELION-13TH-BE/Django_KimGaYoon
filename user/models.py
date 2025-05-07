from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
    # add additional fields in here
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    nickname = models.CharField(max_length=30, blank=True, null=True)

    groups= models.ManyToManyField(Group, related_name="customuser_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions_set", blank=True)
    pass

class Guestbook(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='guestbooks', on_delete=models.CASCADE)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='written_guestbooks', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.writer.username} → {self.owner.username}: {self.message[:20]}"