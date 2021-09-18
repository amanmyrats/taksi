from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework import filters, generics


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

def saher_ici_view(request):
    if request.method=='GET':
        category = Category.objects.get(id=1)
        taksistler = TaxiProfile.objects.filter(category=category)
        serializer = TaxiSerializer(taksistler, many=True)
        return JsonResponse(serializer.data, safe=False)

def etrap_obalary_view(request):

    if request.method=='GET':
        category = Category.objects.get(id=2)
        taksistler = TaxiProfile.objects.filter(category=category)
        serializer = TaxiSerializer(taksistler, many=True)
        return JsonResponse(serializer.data, safe=False)

def saher_ara_view(request):
    if request.method=='GET':
        category = Category.objects.get(id=3)
        taksistler = TaxiProfile.objects.filter(category=category)
        serializer = TaxiSerializer(taksistler, many=True)
        print('serializer data:')
        return JsonResponse(serializer.data, safe=False)

class TaxiListAPIView(generics.ListAPIView):

    serializer_class = TaxiSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user_id__first_name', 'user_id__last_name', 'mobile', 'nireden__name', 'nira__name']

    def get_queryset(self):
        nira = self.request.GET.get('category')
        category = None
        if nira == 'saherici':
            category = Category.objects.get(id = 1)
        elif nira == 'etrapobalary':
            category = Category.objects.get(id = 2)
        elif nira == 'saherara':
            category = Category.objects.get(id = 3)

        if category is not None:
            return TaxiProfile.objects.filter(category=category)
        else:
            return TaxiProfile.objects.all()