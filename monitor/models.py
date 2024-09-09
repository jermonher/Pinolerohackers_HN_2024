from django.db import models
import uuid
from django.core.exceptions import ValidationError
from django.utils import timezone

class Species(models.Model):
    CONSERVATION_STATUSES = [
        ('LC', 'Least Concern'),
        ('NT', 'Near Threatened'),
        ('VU', 'Vulnerable'),
        ('EN', 'Endangered'),
        ('CR', 'Critically Endangered'),
        ('EW', 'Extinct in the Wild'),
        ('EX', 'Extinct'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=200, unique=True)
    conservation_status = models.CharField(max_length=2, choices=CONSERVATION_STATUSES)

    class Meta:
        verbose_name = "Species"
        verbose_name_plural = "Species"

    def __str__(self):
        return self.name

class Observation(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    date = models.DateField()
    notes = models.TextField()

    class Meta:
        verbose_name = "Observation"
        verbose_name_plural = "Observations"

    def __str__(self):
        return f"{self.species} observed at {self.location}"

    def clean(self):
        if self.date > timezone.now().date():
            raise ValidationError("La fecha de observación no puede estar en el futuro.")
