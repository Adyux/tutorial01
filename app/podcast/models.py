from django.db import models

class Host(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'host'

class Podcast(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=500, null=True, blank=True)
    host = models.ForeignKey(to=Host, related_name='podcast',
            on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        db_table = "podcast"


class PodcastItem(models.Model):
    title = models.CharField(max_length=300)
    duration = models.IntegerField(blank=True, null=True)
    synopsis = models.CharField(max_length=500, null=True, blank=True)
    podcast = models.ForeignKey(to=Podcast, related_name='item',
            on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        db_table = 'podcast_item'
