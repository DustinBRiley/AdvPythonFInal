import datetime
from django.db import models
from django.utils import timezone
class PokemonCard(models.Model):    # PokemonCard table
    creator = models.CharField(max_length=150)  # creator column for username of creator
    creation_date = models.DateTimeField(auto_now=True) # creation_date column
    name = models.CharField(max_length=20)  # pokemon name
    types = [   # tuple list of types for list of choices
        ("Normal", "Normal"),   # first is the data entered when choosing this choice
        ("Electric", "Electric"),   # second is what the user sees on the dropdown list
        ("Grass", "Grass"),
        ("Water", "Water"),
        ("Fire", "Fire"),
        ("Fighting", "Fighting"),
        ("Psychic", "Psychic")
    ]
    type = models.CharField(max_length=8, choices=types, default="Grass")   # pokemon type
    image = models.ImageField(upload_to='pcc/images/')  # image of pokemon
    move_name = models.CharField(max_length=20, default="Absorb")   # move name
    move_text = models.CharField(max_length=200, default="Remove 2 damage counters")    # move text
    move_dmg = models.IntegerField(default=20)  # amount of damage the move does

    def __str__(self):
        return self.name
    def was_created_recently(self):
        return self.creation_date >= timezone.now() - datetime.timedelta(days=1)