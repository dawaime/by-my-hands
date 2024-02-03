from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect, JsonResponse


def home_redirect(request):
    return redirect("home")


def home(request):
    
    if request.method == 'GET':
      return render(request, "home.html")
        
    elif request.method == 'POST':

      # you may increment the counter

      return JsonResponse({'redirect': '/register_information/'})
      
    return render(request, "home.html")


def register_information(request):
    
  if request.method == 'GET':
    return render(request, "register_information.html")
        
  elif request.method == 'POST':

    # you may increment the counter

    return JsonResponse({'redirect': '/result/'})
      
  return render(request, "register_information.html")


def result(request):
  return render(request, "result_page.html")