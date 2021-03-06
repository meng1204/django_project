from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


# set one-one relationship between User and Profile


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)  # one way deletion

    image = models.ImageField(default='default.jpg',
                              upload_to='profile_pics')  # set image field

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()  # parent save

        # resize image size
        img = Image.open(self.image.path)  # open image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
