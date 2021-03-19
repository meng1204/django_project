from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# shell: Database query
# include mode: from django.models import Post
# get first/All row(s): Post.objects.first()/all()
# get filter rows: Post.objects.filter(title="Blog 1")
# insert row: post_1 = Post(title="Blog 1", content="First Post Content", author=user)   post_1.save()
# get particular user's posts: user.post_set => user.post_set.all()
# Insert post for this user: user.post_set.create(title="Blog 3", content= "Third Post Content")

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()  # text without restriction
    date_posted = models.DateTimeField(default=timezone.now)
    # user is deleted, then delete all posts
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #  Show Objects Name
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # redirect: redirect view page to other pages
        # reverse: return url as string
        return reverse('post-detail', kwargs={'pk': self.pk})
