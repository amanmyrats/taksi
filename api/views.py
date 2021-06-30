from django.http import JsonResponse
from django.contrib.auth.models import User

from .serializers import TaxiSerializer
from taksist.models import TaxiProfile, Category, Status

def all_taksi_view(request):
    if request.method == 'GET':
        taksistler = TaxiProfile.objects.all()
        serializer = TaxiSerializer(taksistler, many=True)
        return JsonResponse(serializer.data, safe=False)

def taksi_detail_view(request, **kwargs):
    if request.method == 'GET':
        taksistler = TaxiProfile.objects.get(pk=kwargs.get('pk'))
        serializer = TaxiSerializer(taksistler, many=False)
        return JsonResponse(serializer.data, safe=False)

def saher_ara_view(request):
    if request.method=='GET':
        category = Category.objects.get(id=3)
        taksistler = TaxiProfile.objects.filter(category=category)
        serializer = TaxiSerializer(taksistler, many=True)
        print('serializer data:')
        return JsonResponse(serializer.data, safe=False)

def saher_ici_view(request):
    if request.method=='GET':
        category = Category.objects.get(id=2)
        taksistler = TaxiProfile.objects.filter(category=category)
        serializer = TaxiSerializer(taksistler, many=True)
        return JsonResponse(serializer.data, safe=False)

def etrap_obalary_view(request):
    if request.method=='GET':
        category = Category.objects.get(id=1)
        taksistler = TaxiProfile.objects.filter(category=category)
        serializer = TaxiSerializer(taksistler, many=True)
        return JsonResponse(serializer.data, safe=False)