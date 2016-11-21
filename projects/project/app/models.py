from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name

class Post(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return "\"{}...\" on {} by {}".format(self.text[:32], self.date_added, self.user)

class Comment(models.Model):
    post = models.ForeignKey(Post)
    text = models.TextField()
    date_added = models.DateTimeField(auto_created=True)

    def __str__(self):
        return "Comment on {}".format(self.date_added)