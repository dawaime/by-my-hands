from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Visitors


def home_redirect(request):
    return redirect("home")


def home(request):
    
    if request.method == 'GET':
      return render(request, "home.html")
        
    elif request.method == 'POST':

      # Retrieve or create a Visitors instance
      visitor_obj, created = Visitors.objects.get_or_create(pk=1)
        
      # Increment the counter
      counter = visitor_obj.global_click_counter_register + 1
      visitor_obj.global_click_counter_register = counter
      visitor_obj.save()

      return JsonResponse({'redirect': '/register_information/'})
      
    return render(request, "home.html")


def register_information(request):
    
  if request.method == 'GET':
    return render(request, "register_information.html")
        
  elif request.method == 'POST':

    # Retrieve or create a Visitors instance
    visitor_obj, created = Visitors.objects.get_or_create(pk=1)
        
    # Increment the counter
    counter = visitor_obj.global_click_counter_result + 1
    visitor_obj.global_click_counter_result = counter
    visitor_obj.save()

    return JsonResponse({'redirect': '/result/'})
      
  return render(request, "register_information.html")


def result(request):
  return render(request, "result_page.html")


@login_required(login_url="/admin/")
def counters(request):
  
  visitor = Visitors.objects.get(pk=1)
  visitor.global_click_counter_result

  context = {
    "register_counter": visitor.global_click_counter_register,
    "result_counter": visitor.global_click_counter_result,
  }
   
  return render(request, "counters.html", context)