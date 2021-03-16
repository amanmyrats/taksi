from django.http import JsonResponse

from .serializers import TaxiSerializer
from taksist.models import TaxiProfile


def saher_ara_view(request):
    if request.method=='GET':
        taksistler = TaxiProfile.objects.all()
        serializer = TaxiSerializer(taksistler, many=True)
        return JsonResponse(serializer.data, safe=False)

def saher_ici_view(request):
    if request.method=='GET':
        taksistler = TaxiProfile.objects.all()
        serializer = TaxiSerializer(taksistler, many=True)
        return JsonResponse(serializer.data, safe=False)

def etrap_obalary_view(request):
    if request.method=='GET':
        taksistler = TaxiProfile.objects.all()
        serializer = TaxiSerializer(taksistler, many=True)
        return JsonResponse(serializer.data, safe=False)