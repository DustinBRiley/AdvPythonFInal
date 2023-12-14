from django.forms import ModelForm
from .models import PokemonCard

class PokemonCardForm(ModelForm):
    class Meta:
        model = PokemonCard
        fields = ['name','type','image','move_name','move_text','move_dmg']