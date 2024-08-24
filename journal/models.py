"""models.py"""

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=31)


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag', related_name='posts')
