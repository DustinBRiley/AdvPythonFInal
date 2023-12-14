from django.forms import ModelForm
from .models import PokemonCard

class PokemonCardForm(ModelForm):
    class Meta:
        model = PokemonCard # PokemonCard table
        fields = ['name','type','image','move_name','move_text','move_dmg'] # list of fields the user can change (also displays default text)