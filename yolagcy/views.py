from django.shortcuts import render
from django.contrib.auth.models import User
import requests

def search_view(request, **kwargs):
    print('inside search view')
    if request.method == 'GET':
        if kwargs.get('nira')=='saherara':
            data = requests.get('http://127.0.0.1:8000/api/saherara/', params=request.GET)
            print(data)
            print('saherara')
        elif kwargs.get('nira')=='saherici':
            data = requests.get('http://127.0.0.1:8000/api/saherici/', params=request.GET)
        elif kwargs.get('nira')=='etrapobalary':
            data = requests.get('http://127.0.0.1:8000/api/etrapobalary/', params=request.GET)
        else:
            data = User.objects.all()
    # taxi_drivers=User.objects.all()
    return render(request, 'search.html', {'taxi_drivers':data.json()})
