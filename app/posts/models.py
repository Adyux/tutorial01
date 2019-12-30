from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

# Create your models here.


class PostRelation(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.CharField(max_length=100, null=True)
    stix_relation = GenericForeignKey()

    re_posts = models.ManyToManyField("posts.Repost", related_name="post_relation")


class PostMetaData(models.Model):
    name_hash = models.CharField(max_length=32, null=True)
    relation = GenericRelation(PostRelation, related_query_name="%(class)s_query")

    class Meta:
        abstract = True


class UserPost(PostMetaData):
    usr_id = models.CharField(max_length=32, null=True)


class Repost(PostMetaData):
    usr_id = models.CharField(max_length=32, null=True)
