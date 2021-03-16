from django.urls import path
from .views import saher_ara_view, saher_ici_view, etrap_obalary_view

urlpatterns = [
    path('api/saherara/', saher_ara_view),
    path('api/saherici/', saher_ici_view),
    path('api/etrapobalary/', etrap_obalary_view)
    ]
