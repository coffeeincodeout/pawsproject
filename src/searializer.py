from rest_framework import serializers
from .models import animals

class AnimalsSerializer(serializers.ModelSerializer):

    class Meta:
        model = animals
        fields = ('name', 'description', 'age',
                  'weight', 'url')