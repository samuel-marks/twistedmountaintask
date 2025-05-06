import graphene
from graphene_django.types import DjangoObjectType
from .models import Task
from graphql_jwt.decorators import login_required

class TaskType(DjangoObjectType):
    class Meta:
        model = Task

class Query(graphene.ObjectType):
    all_tasks = graphene.List(TaskType)

    @login_required
    def resolve_all_tasks(self, info):
        user = info.context.user
        return Task.objects.filter(assigned_to=user)

schema = graphene.Schema(query=Query)
