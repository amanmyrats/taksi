from django.urls import path
from .views import saher_ara_view, saher_ici_view, etrap_obalary_view, all_taksi_view, taksi_detail_view, TaxiListAPIView

urlpatterns = [
    path('api/taksiler/', all_taksi_view),
    path('api/taksiler/<int:pk>/', taksi_detail_view),
    path('api/saherara/', saher_ara_view),
    path('api/saherici/', saher_ici_view),
    path('api/etrapobalary/', etrap_obalary_view),
    path('api/hemmesi/', TaxiListAPIView.as_view()),
    ]
