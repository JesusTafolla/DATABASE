import graphene
from graphene_django import DjangoObjectType

from .models import Notes


class NoteType(DjangoObjectType):
    class Meta:
        model = Notes


class Query(graphene.ObjectType):
    notes = graphene.List(NoteType)

    def resolve_notes(self, info, **kwargs):
        return Notes.objects.all()
# ...code
#1
class CreateNote(graphene.Mutation):
    id = graphene.Int()
    user = graphene.String()
    description = graphene.String()

    #2
    class Arguments:
        user = graphene.String()
        description = graphene.String()

    #3
    def mutate(self, info, user, description):
        note = Notes(user=user, description=description)
        note.save()

        return CreateNote(
            id=note.id,
            user=note.user,
            description=note.description,
        )


#4
class Mutation(graphene.ObjectType):
    create_note = CreateNote.Field()
