from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import Note as NoteModel


class Note(DjangoObjectType):
    class Meta:
        model = NoteModel

        interfaces = (graphene.relay.Node, )


class Query(graphene.ObjectType):
    note = graphene.Field(Note, id=graphene.String(), title=graphene.String())
    all_notes = graphene.List(Note)

    def resolve_notes(self, info):
        """Decide which notes to return."""

        user = info.context.user

        if settings.DEBUG:
            return NoteModel.objects.all()
        elif user.is_anonymous:
            return NoteModel.objects.none()
        else:
            return NoteModel.objects.filter(user=user)

    def resolve_note(self, info, **kwargs):
        title = kwargs.get('title')
        id = kwargs.get('id')

        if title is not None:
            return NoteModel.objects.get(title=title)

        return None


class CreateNote(graphene.Mutatation):

    class Arguments:
        title = graphene.String()
        content = graphene.String()

    ok = graphene.Boolean()
    note = graphene.Field(Note)

    def mutate(self, info, title, content):
        user = info.context.user

        if user.is_anonymous:
            is_ok = False
            return CreateNote(ok=is_ok)

        else: 
            new_note = NoteModel(title = title, content = content, user = user)
            new_note.save()
            is_ok = True

            return CreateNote(note=new_note, ok=is_ok)

class Mutation(graphene.ObjectType):
    create_note = CreateNote.Field()

schema = graphene.Schema(query=Query)
