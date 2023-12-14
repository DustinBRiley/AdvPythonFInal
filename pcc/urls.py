from django.urls import path

from . import views
from .views import register, login, logout, create
from django.conf.urls.static import static
from django.conf import settings

app_name = "pcc"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),  # serve index view object when visiting localhost:8000
    path("login.html", login, name="login"),    # serve login function when visiting localhost:8000/login.html
    path("logout.html", logout, name="logout"), # serve logout function when visiting localhost:8000/logout.html
    path("register.html", register, name="register"),   # serve register function when visiting localhost:8000/register.html
    path("create.html", create, name="create"), # serve create function when visiting localhost:8000/create.html
    path("collection.html", views.CollectionView.as_view(), name="collection")  # serve collection view object when visiting localhost:8000/collection.html
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)