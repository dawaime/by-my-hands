from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect, JsonResponse


def home(request):
    return render(request, "home.html")

def home_redirect(request):
    return redirect("home")