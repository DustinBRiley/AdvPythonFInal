from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import generic
from pokemontcgsdk import Card
from .forms import PokemonCardForm
from .models import PokemonCard
from PIL import Image, ImageDraw, ImageFont

class IndexView(generic.ListView):
    template_name = "pcc/index.html"
    context_object_name = "base"

    def get_queryset(self):
        return Card.where(q="set.id:base1 supertype:Pokémon")


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
        return render(request, "pcc/login.html")

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
        return render(request, "pcc/register.html")

def create(request):
    form = PokemonCardForm
    if request.method == 'POST':
        form = PokemonCardForm(request.POST, request.FILES)
        if form.is_valid():
            a = form.save(commit=False)
            a.creator = request.user.username
            card = Image.open('pcc/images/' + a.type + '.png')
            newcard = card.copy()
            img = Image.open(a.image)
            img = img.resize((363,256))
            newcard.paste(img, (55,83))
            draw_name = ImageDraw.Draw(newcard)
            draw_name.text((45,42), a.name, font=ImageFont.truetype('arial.ttf', 32), fill=(0,0,0))
            draw_move = ImageDraw.Draw(newcard)
            draw_move.text((100,410), a.move_name, font=ImageFont.truetype('arial.ttf', 30), fill=(0,0,0))
            draw_text = ImageDraw.Draw(newcard)
            draw_text.text((100,460), a.move_text, font=ImageFont.truetype('arial.ttf', 15), fill=(0,0,0))
            draw_dmg = ImageDraw.Draw(newcard)
            draw_dmg.text((390,430), (str) (a.move_dmg), font=ImageFont.truetype('arial.ttf', 35), fill=(0,0,0))
            newcard.save('pcc/images/' + (a.name).replace(" ","_") + '.png')
            a.image = ('pcc/images/' + (a.name).replace(" ","_") + '.png')
            a.save()
            return redirect("collection.html")
    context = {'form':form}
    return render(request, "pcc/create.html", context)

class CollectionView(generic.ListView):
    template_name = "pcc/collection.html"
    context_object_name = "created_pokemon"

    def get_queryset(self):
        return PokemonCard.objects.filter(creator=self.request.user)

class DetailView(generic.DetailView):
    template_name = "pcc/detail.html"
    context_object_name = ""

