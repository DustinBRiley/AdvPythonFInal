from django.urls import path

from . import views
from .views import register, login, logout

app_name = "pcc"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("login.html", login, name="login"),
    path("logout.html", logout, name="logout"),
    path("register.html", register, name="register"),
    path("create.html", views.CreateView.as_view(), name="create"),
    path("collection.html", views.CollectionView.as_view(), name="collection"),
    path("<int:pokemon_id>", views.DetailView.as_view(), name="detail")
]