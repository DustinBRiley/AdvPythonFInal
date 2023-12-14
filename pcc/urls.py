from django.urls import path

from . import views
from .views import register, login, logout, create
from django.conf.urls.static import static
from django.conf import settings

app_name = "pcc"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("login.html", login, name="login"),
    path("logout.html", logout, name="logout"),
    path("register.html", register, name="register"),
    path("create.html", create, name="create"),
    path("collection.html", views.CollectionView.as_view(), name="collection")
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)