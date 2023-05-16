from rest_framework import serializers

from actors.models import Actor


class ActorsSerializer(serializers.ModelSerializer):
    """Сериализатор просмотра актёров"""

    class Meta:
        model = Actor
        fields = ('id', 'name', 'last_name', 'age', 'town',
                  'height', 'body', 'hair_col', 'eyes_col',
                  'person', 'education', 'language',
                  'roles', 'skills', 'images')
        depth = 1
