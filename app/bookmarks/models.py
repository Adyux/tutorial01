from django.contrib.contenttypes.fields import GenericRelation
from django.db import models


class Bookmark(models.Model):
    url = models.URLField()
    tags = GenericRelation("tags.TaggedItem")
