from rest_framework import generics
from .models import HistoricalPerformance
from .serializers import HistoricalPerformanceSerializer

class HistoricalPerformanceListCreate(generics.ListCreateAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer

class HistoricalPerformanceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
