from django.shortcuts import render
from django.contrib.auth.models import User
import requests

from .filters import TaxiFilter
from api.views import TaxiListAPIView

def search_view(request, **kwargs):
    print('inside search view')
    search = request.GET.get('search')
    

    if request.method == 'GET':
        # test = request.GET.get('searchbox')
        # print('this is test search: ',test)
        # data = requests.get('http://127.0.0.1:8000/api/saherara/', params=request.GET)
        # print(data)
        # # print(data.json())
        # print('doing saherara ici in search view')
        print('searching nira:',kwargs.get('nira'))
        if search is not None:
            data = requests.get('http://127.0.0.1:8000/api/test/', params=request.GET)
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
    return render(request, 'search.html', {'taxi_drivers':data.json()})

def taxi_search_view(request):
    taksistler = TaxiProfile.objects.all()
    filter = TaxiFilter(request.GET, queryset = taksistler)
    return render(request, 'search.html', {'filter':filter})