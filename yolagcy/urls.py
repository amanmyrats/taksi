
from django.urls import path
from .views import TaxiListView, search_view

urlpatterns = [
    path('search/', search_view, name='search'),
    path('search/<str:nira>/', search_view, name='searchcategory'),
    path('taxis/', TaxiListView.as_view())
]
