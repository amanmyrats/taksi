from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
import requests
import time
from django.views.generic import ListView
from django.core.paginator import Paginator

from .filters import TaxiFilter
from api.views import TaxiListAPIView
from taksist.models import TaxiProfile, City, Category

class TaxiListView(ListView):
    model = TaxiProfile
    template_name = 'taxis.html'
    # queryset = TaxiProfile.objects.all()
    paginate_by = 3
    context_object_name = 'taxi_drivers'



def search_view(request, **kwargs):
    print('inside search view')
    
    category = request.GET.get('category')
    nireden = request.GET.get('nireden')
    nira = request.GET.get('nira')
    search = request.GET.get('search')
    print('user is searching category:', category)
    print('user is searching nireden:', nireden)
    print('user is searching nira:', nira)
    print('user is searching a word:', search)
    
    
    

    if request.method == 'GET':
        data = requests.get('http://127.0.0.1:8000/api/hemmesi/', params=request.GET)
        # if search is not None:
        #     data = requests.get('http://127.0.0.1:8000/api/hemmesi/', params=request.GET)
        # else:
        #     if kwargs.get('category')=='saherici':
        #         data = requests.get('http://127.0.0.1:8000/api/saherici/', params=request.GET)
        #     elif kwargs.get('category')=='etrapobalary':
        #         data = requests.get('http://127.0.0.1:8000/api/etrapobalary/', params=request.GET)
        #     elif kwargs.get('category')=='saherara':
        #         data = requests.get('http://127.0.0.1:8000/api/saherara/', params=request.GET)
        #     else:
        #         data = requests.get('http://127.0.0.1:8000/api/hemmesi/', params=request.GET)

    drivers = data.json()
    paginator = Paginator(drivers, 6) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()
    nireden_cities = City.objects.all().exclude(pk=1).exclude(pk=2)
    nira_cities = City.objects.all()
    try:
        current_category = get_object_or_404(Category, pk=category)
    except:
        current_category = ''
    
    try:
        current_nireden = get_object_or_404(City, pk=nireden)
    except:
        current_nireden = ''

    try:
        current_nira = get_object_or_404(City, pk=nira)
    except:
        current_nira = ''

    context = { 'drivers': drivers, 
                'page_obj': page_obj,
                'categories' : categories,
                'nireden_cities' : nireden_cities,
                'nira_cities' : nira_cities,
                'current_category':current_category,
                'current_nireden':current_nireden,
                'current_nira':current_nira}
    return render(request, 'search.html', context)

def taxi_search_view(request):
    taksistler = TaxiProfile.objects.all()
    filter = TaxiFilter(request.GET, queryset = taksistler)
    return render(request, 'search.html', {'filter':filter})