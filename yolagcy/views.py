from django.shortcuts import render
from django.contrib.auth.models import User

def search_view(request):
    taxi_drivers=User.objects.all()
    return render(request, 'search.html', {'taxi_drivers':taxi_drivers})
