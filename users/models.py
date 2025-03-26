from django.contrib.auth.models import User
from django.db import models

# Create your models here
#
class Profile(models.Model):
    img =models.ImageField(upload_to="Profile_image",blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.user}"