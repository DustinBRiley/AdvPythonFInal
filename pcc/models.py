import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class PokemonCard(models.Model):
    creator = User.get_username
    creation_date = models.DateTimeField("date created")
    Name = models.CharField(max_length=200)
    Types = [
        ("Normal", "Normal"),
        ("Electric", "Electric"),
        ("Grass", "Grass"),
        ("Water", "Water"),
        ("Fire", "Fire"),
        ("Fighting", "Fighting"),
        ("Psychic", "Psychic")
    ]
    Type = models.CharField(max_length=8, choices=Types)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.Name
    def was_created_recently(self):
        return self.creation_date >= timezone.now() - datetime.timedelta(days=1)