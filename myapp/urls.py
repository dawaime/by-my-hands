from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(
        "",
        views.home_redirect,
        name="home_redirect"
    ),
    path(
        "home/",
        views.home,
        name="home"
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)