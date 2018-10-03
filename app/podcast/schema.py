import graphene

from graphene_django import DjangoObjectType
from .models import Host, Podcast, PodcastItem


class PodcastType(DjangoObjectType):
    class Meta:
        model = Podcast

class CreatePodcast(graphene.Mutation):
    podcast = graphene.Field(PodcastType)

    class Arguments:
        name = graphene.String()

    def mutate(self, info, **kwargs):
        podcast = Podcast(**kwargs)
        podcast.save()
        return CreatePodcast(podcast=podcast)


class HostType(DjangoObjectType):
    class Meta:
        model = Host


class PodcastItemType(DjangoObjectType):
    class Meta:
        model = PodcastItem


class Query(graphene.ObjectType):
    podcasts = graphene.List(PodcastType)
    hosts = graphene.List(HostType)

    def resolve_podcasts(self, info, **kwargs):
        return Podcast.objects.all()

    def resolve_hosts(self, info, **kwargs):
        return Host.objects.all()

class Mutation(graphene.ObjectType):
    create_podcast = CreatePodcast.Field()
