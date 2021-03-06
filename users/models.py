from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# set one-one relationship between User and Profile


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)  # one way deletion

    image = models.ImageField(default='default.jpg',
                              upload_to='profile_pics')  # set image field

    def __str__(self):
        return f'{self.user.username} Profile'
