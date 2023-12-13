import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class PokemonCard(models.Model):
    creator = User.get_username
    creation_date = models.DateTimeField("date created")
    name = models.CharField(max_length=20)
    types = [
        ("Normal", "Normal"),
        ("Electric", "Electric"),
        ("Grass", "Grass"),
        ("Water", "Water"),
        ("Fire", "Fire"),
        ("Fighting", "Fighting"),
        ("Psychic", "Psychic")
    ]
    type = models.CharField(max_length=8, choices=types, default="Grass")
    image = models.ImageField(upload_to='images/')
    move_name = models.CharField(max_length=20, default="Absorb")
    move_text = models.CharField(max_length=200, default="Remove 2 damage counters")
    move_dmg = models.IntegerField(default=20)

    def __str__(self):
        return self.Name
    def was_created_recently(self):
        return self.creation_date >= timezone.now() - datetime.timedelta(days=1)