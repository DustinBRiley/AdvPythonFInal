from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse
from django.views import generic

from .models import PokemonCard

class IndexView(generic.ListView):
    template_name = "pcc/index.html"
    context_object_name = "latest_pokemon_list"

    def get_queryset(self):
        """Return the last five created pokemon cards."""
        return PokemonCard.objects.order_by("-creation_date")[:5]

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('collection.html')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect("login.html")
    else:
        return render(request, "PokemonCreator/login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request, 'username already exists')
            return redirect("register.html")
        else:
            user = User.objects.create_user(username=username, password=password)
            user.set_password(password)
            user.save()
            print("success")
            return redirect("login.html")
    else:
        return render(request, "PokemonCreator/register.html")
class CreateView(generic.CreateView):
    template_name = "PokemonCreator/create.html"

class CollectionView(generic.ListView):
    model = PokemonCard
    template_name = "PokemonCreator/collection.html"

class DetailView(generic.DetailView):
    model = PokemonCard
    template_name = "PokemonCreator/detail.html"
    context_object_name = "created_pokemon"

    def get_queryset(self):
        return PokemonCard.objects.filter(creator=User.get_username)
