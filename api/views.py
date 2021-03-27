from django.http import JsonResponse
from django.contrib.auth.models import User

from .serializers import TaxiSerializer
from taksist.models import TaxiProfile

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
        taksistler = TaxiProfile.objects.filter(cat_id=1)
        # sara = taksistler.taxiprofile_set.all()
        serializer = TaxiSerializer(taksistler, many=True)
        return JsonResponse(serializer.data, safe=False)

def saher_ici_view(request):
    if request.method=='GET':
        taksistler = TaxiProfile.objects.filter(cat_id=2)
        serializer = TaxiSerializer(taksistler, many=True)
        return JsonResponse(serializer.data, safe=False)

def etrap_obalary_view(request):
    if request.method=='GET':
        taksistler = TaxiProfile.objects.filter(cat_id=3)
        serializer = TaxiSerializer(taksistler, many=True)
        return JsonResponse(serializer.data, safe=False)