from django.shortcuts import render
from django.contrib.auth.models import User
import requests
import time

from .filters import TaxiFilter
from api.views import TaxiListAPIView
from taksist.models import TaxiProfile

def search_view(request, **kwargs):
    print('inside search view')
    search = request.GET.get('search')
    nira = kwargs.get('nira')
    print('user is searching:', search)
    print('category is:', nira)
    

    if request.method == 'GET':
        if search is not None:
            data = requests.get('http://127.0.0.1:8000/api/hemmesi/', params=request.GET)
            return render(request, 'search.html', {'taxi_drivers':data.json()})
        else:
            if kwargs.get('nira')=='saherici':
                print('i will request  saher ici api in search view')
                data = requests.get('http://127.0.0.1:8000/api/saherici/', params=request.GET)
                print('sucessfully got saher ici in search view')
            elif kwargs.get('nira')=='etrapobalary':
                print('i will request  etrapobalary api in search view')
                data = requests.get('http://127.0.0.1:8000/api/etrapobalary/', params=request.GET)
                print('sucessfully got etrapobalary in search view')
            elif kwargs.get('nira')=='saherara':
                print('i will request saherara api')
                data = requests.get('http://127.0.0.1:8000/api/saherara/', params=request.GET)
                print(data)
                print('sucessfully got saherara ara in search view')
            else:
                print('will return all taxi')
                data = requests.get('http://127.0.0.1:8000/api/hemmesi/', params=request.GET)
                print('sucessfully got all taxi data')

    # print(data.json())
    print('returning render in search view')
    print('category nira is:', nira)
    return render(request, 'search.html', {'taxi_drivers':data.json(), 'category':nira})

def taxi_search_view(request):
    taksistler = TaxiProfile.objects.all()
    filter = TaxiFilter(request.GET, queryset = taksistler)
    return render(request, 'search.html', {'filter':filter})