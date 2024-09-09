from rest_framework import serializers
from .models import Species, Observation

class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ['id', 'name', 'scientific_name', 'conservation_status']

class ObservationSerializer(serializers.ModelSerializer):
    species = SpeciesSerializer(read_only=True)

    class Meta:
        model = Observation
        fields = ['id', 'species', 'location', 'date', 'notes']
