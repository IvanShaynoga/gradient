from rest_framework import viewsets
from rest_framework.response import Response
from actors.models import Actor, ActorImage
from .serializers import ActorsSerializer


class ActorsViewSet(viewsets.ModelViewSet):
    serializer_class = ActorsSerializer

    def get_queryset(self):
        actors = Actor.objects.all()
        return actors

    def create(self, request, *args, **kwargs):
        actor = request.data
        new_actor = Actor.objects.create(
            name=actor['name'], last_name=actor['last_name'], age=actor['age'],
            town=actor['town'], height=actor['height'], body=actor['body'],
            hair_col=actor['hair_col'], eyes_col=actor['eye_col'],
            person=actor['person'], education=actor['education'],
            language=actor['languge'], roles=actor['roles'],
            skills=actor['skills'],
            images=ActorImage.objects.get(id=actor['images'])
            )
        new_actor.save()
        serializer = ActorsSerializer(new_actor)
        return Response(serializer.data)
