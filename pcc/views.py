from typing import Any
from django.contrib.auth.models import User
from django.contrib import auth
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import generic
from pokemontcgsdk import Card
from .forms import PokemonCardForm
from .models import PokemonCard
from PIL import Image, ImageDraw, ImageFont

class IndexView(generic.ListView): # index view object
    template_name = "pcc/index.html"    # the html file
    context_object_name = "base"    # name of the query

    def get_queryset(self):
        return Card.where(q="set.id:base1 supertype:Pokémon")   # returns Pokemon TCG API Card search for set base1 and supertype Pokemon (just pokemon cards not trainer,energy,etc.)


def login(request): # login view as a function
    if request.method == 'POST':    # form submits as POST
        username = request.POST['username'] # get form username value
        password = request.POST['password'] # get form password value

        user = auth.authenticate(username=username, password=password)  # checks if username and password are correct

        if user is not None:    # if user got authenticated correctly
            auth.login(request, user)   # log user in
            return redirect('collection.html')  # redirect to collection webpage
        else:
            messages.info(request, 'Invalid Username or Password') # username or password was incorrect
            return redirect("login.html")   # reload the page to try to log in again
    else:
        return render(request, "pcc/login.html")    # load login webpage when not POST (like when visiting the log in page in the first place)

def logout(request):    # logout function
    auth.logout(request)    # log out
    return redirect('/')    # redirect to home /index.html

def register(request):  # register function
    if request.method == 'POST':    # form submits as POST
        username = request.POST['username'] # get form username value
        password = request.POST['password'] # get form password value
        if User.objects.filter(username=username).exists(): # checks if username already exists in user table
            messages.info(request, 'username already exists')
            return redirect("register.html")    # reload page
        else:
            user = User.objects.create_user(username=username, password=password)   # creates entry into user table with username and password from form
            user.set_password(password) # sets the password (necessary apparently encryption or something)
            user.save() # saves the entry to user table
            print("success")
            return redirect("login.html")   #redirect to login webpage
    else:
        return render(request, "pcc/register.html") # load register webpage when method != POST

def create(request):    # create function
    form = PokemonCardForm  # set form from forms.py
    if request.method == 'POST':    # form submits as POST
        form = PokemonCardForm(request.POST, request.FILES) # sets form data into pokemoncardform
        if form.is_valid(): # if valid data provided
            a = form.save(commit=False) # save form data but dont commit it yet
            a.creator = request.user.username   # set the creator attribute of PokemonCard to current user
            card = Image.open('pcc/images/' + a.type + '.png')  # open card template based on form field type
            newcard = card.copy()   # make a copy so that the template doesnt get changed
            img = Image.open(a.image)   # opens image uploaded in the form
            img = img.resize((366,257)) # resizes uploaded image
            newcard.paste(img, (54,83)) # pastes the resized uploaded image onto the template
            draw_name = ImageDraw.Draw(newcard) # starts an image drawing on newcard
            draw_name.text((45,42), a.name, font=ImageFont.truetype('arial.ttf', 32), fill=(0,0,0)) # draws the text from form field name at coordinates (45,42)
            draw_move = ImageDraw.Draw(newcard) # starts an image drawing on newcard
            draw_move.text((100,410), a.move_name, font=ImageFont.truetype('arial.ttf', 30), fill=(0,0,0))  # draws the text from form field move_name
            draw_text = ImageDraw.Draw(newcard) # starts an image drawing on newcard
            draw_text.text((100,460), a.move_text, font=ImageFont.truetype('arial.ttf', 15), fill=(0,0,0))  # draws the text from form field move_text
            draw_dmg = ImageDraw.Draw(newcard)  # starts an image drawing on newcard
            draw_dmg.text((390,430), (str) (a.move_dmg), font=ImageFont.truetype('arial.ttf', 35), fill=(0,0,0))    # draws the number converted string from form field move_dmg
            newcard.save('pcc/images/' + (a.name).replace(" ","_") + '.png')    # saves newcard image as form field name replacing " " with an underscore
            a.image = ('pcc/images/' + (a.name).replace(" ","_") + '.png')  # changes form field image replacing " " with an underscore
            a.save()    # saves entry into PokemonCard table
            return redirect("collection.html")  # redirects to collection webpage
    context = {'form':form} # get form context
    return render(request, "pcc/create.html", context)  # return create webpage

class CollectionView(generic.ListView): # collection view object
    template_name = "pcc/collection.html"   # the html file
    context_object_name = "created_pokemon" # name of the query

    def get_queryset(self):
        return PokemonCard.objects.filter(creator=self.request.user)    # returns entries from PokemonCard table created by current user

