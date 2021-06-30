from django.shortcuts import render
from django.contrib.auth.models import User
import requests

from .filters import TaxiFilter

def search_view(request, **kwargs):
    print('inside search view')
    if request.method == 'GET':
        # data = requests.get('http://127.0.0.1:8000/api/saherara/', params=request.GET)
        # print(data)
        # # print(data.json())
        # print('doing saherara ici in search view')
        if kwargs.get('nira')=='saherara':
            print('i will request saherara api')
            data = requests.get('http://127.0.0.1:8000/api/saherara/', params=request.GET)
            print(data)
            print('did saherara ara in search view')
        elif kwargs.get('nira')=='saherici':
            print('i will request  saher ici api in search view')
            data = requests.get('http://127.0.0.1:8000/api/saherici/', params=request.GET)
            print('did saher ici in search view')
        elif kwargs.get('nira')=='etrapobalary':
            print('i will request  etrapobalary api in search view')
            data = requests.get('http://127.0.0.1:8000/api/etrapobalary/', params=request.GET)
            print('did etrapobalary in search view')
        else:
            # data = None
            # pass
            data = requests.get('http://127.0.0.1:8000/api/taksiler/', params=request.GET)
    # taxi_drivers=User.objects.all()
    print('returning render in search view')
    return render(request, 'search.html', {'taxi_drivers':data.json()})

def taxi_search_view(request):
    taksistler = TaxiProfile.objects.all()
    filter = TaxiFilter(request.GET, queryset = taksistler)
    return render(request, 'search.html', {'filter':filter})