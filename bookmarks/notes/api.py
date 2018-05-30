from rest_framkework import serializers, viewsets
from .models import Note

class NoteSerializer(serializers.HyperLinkedModelSerializer):
  def create(self, validated_data):
      user: self.context['request'].user

      note = Note.object.create(**validated_data)
      return note

  class Meta: 
    model = NoteSerializer
    fields = ('title', 'content')

class NoteViewSet(viewsets.ModelViewSet):
  serializer_class = NoteSerializer
  queryset = Note.objects.all()  