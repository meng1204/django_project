from django.contrib import admin
from .models import Post

# Register your models here.


# show Post Objects in Admin Page
admin.site.register(Post)