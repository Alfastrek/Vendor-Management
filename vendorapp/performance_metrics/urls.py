from django.urls import path
from .views import HistoricalPerformanceListCreate, HistoricalPerformanceRetrieveUpdateDestroy

urlpatterns = [
    path('api/historical-performance/', HistoricalPerformanceListCreate.as_view(), name='historical-performance-list-create'),
    path('api/historical-performance/<int:pk>/', HistoricalPerformanceRetrieveUpdateDestroy.as_view(), name='historical-performance-retrieve-update-destroy'),
]
