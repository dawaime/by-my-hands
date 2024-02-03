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
    path(
        "register_information/",
        views.register_information,
        name="register_information"
    ),
    path(
        "result/",
        views.result,
        name="result"
    ),
    path(
        "counters/",
        views.counters,
        name="counters"
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)