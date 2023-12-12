
from django.http import HttpResponse

from .models import PokemonCard


def index(request):
    latest_pokemoncard_list = PokemonCard.objects.order_by("-pub_date")[:5]
    output = ", ".join([p.Name for p in latest_pokemoncard_list])
    return HttpResponse(output)