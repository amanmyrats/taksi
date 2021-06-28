from django.shortcuts import render
from django.contrib.auth.models import User
import requests

def search_view(request, **kwargs):
    print('inside search view')
    if request.method == 'GET':
        if kwargs.get('nira')=='saherara':
        
            data = requests.get('http://127.0.0.1:8000/api/saherara/', params=request.GET)
            print(data)
            print('doing saherara ici in search view')
        elif kwargs.get('nira')=='saherici':
            print('doing saher ici in search view')
            data = requests.get('http://127.0.0.1:8000/api/saherici/', params=request.GET)
            print('did saher ici in search view')
        elif kwargs.get('nira')=='etrapobalary':
            print('doing etrapobalary ici in search view')
            data = requests.get('http://127.0.0.1:8000/api/etrapobalary/', params=request.GET)
            print('did etrapobalary ici in search view')
        else:
            data = User.objects.all()
    # taxi_drivers=User.objects.all()
    print('returning render in search view')
    return render(request, 'search.html', {'taxi_drivers':data.json()})
