
from django.urls import path
from .views import search_view

urlpatterns = [
    path('search/', search_view, name='search'),
    path('search/<str:nira>/', search_view, name='searchcategory'),
]
