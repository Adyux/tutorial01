from django.db import models

# Create your models here.


class Song(models.Model):
    tags = models.ManyToManyField("tags.TaggedItem")
    bookmarks = models.ManyToManyField("bookmarks.Bookmark")
