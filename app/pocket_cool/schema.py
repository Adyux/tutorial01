import graphene
import podcast.schema
from graphene_django import DjangoObjectType


class Query(podcast.schema.Query, graphene.ObjectType): pass

class Mutation(podcast.schema.Mutation, graphene.ObjectType): pass

schema = graphene.Schema(query=Query, mutation=Mutation)
