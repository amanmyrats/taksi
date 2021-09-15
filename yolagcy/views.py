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
    print('this is search', search)
    

    if request.method == 'GET':
        # test = request.GET.get('searchbox')
        # print('this is test search: ',test)
        # data = requests.get('http://127.0.0.1:8000/api/saherara/', params=request.GET)
        # print(data)
        # # print(data.json())
        # print('doing saherara ici in search view')
        
        # time.sleep(1)
        # print("waited 1 second")
        if search is not None:
            
            # to make search better, i must send category parameter to TaxiAPIListView
            category = kwargs.get('nira')
            print('searching category:',kwargs.get('nira'))
            if category is None:
                data = requests.get('http://127.0.0.1:8000/api/test/', params=request.GET)
            else:
                data = requests.get('http://127.0.0.1:8000/api/test/', params=request.GET, category = category)
            return render(request, 'search.html', {'taxi_drivers':data.json()})
        else:
            # return render(request, 'search.html', {'taxi_drivers':data.json()})

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
                data = requests.get('http://127.0.0.1:8000/api/test/', params=request.GET)

    # taxi_drivers=User.objects.all()
    print('returning render in search view')
    testtaxi = TaxiProfile.objects.all()
    return render(request, 'search.html', {'taxi_drivers':testtaxi})
    return render(request, 'search.html', {'taxi_drivers':data.json()})

def taxi_search_view(request):
    taksistler = TaxiProfile.objects.all()
    filter = TaxiFilter(request.GET, queryset = taksistler)
    return render(request, 'search.html', {'filter':filter})