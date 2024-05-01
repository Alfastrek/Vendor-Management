from rest_framework import generics
from .models import PurchaseOrder
from rest_framework.response import Response
from .serializers import PurchaseOrderSerializer
from django.utils import timezone
from rest_framework import status

class PurchaseOrderListCreate(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class AcknowledgePurchaseOrder(generics.UpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.acknowledgment_date = timezone.now()  
        instance.save()
        return Response({"message": "Purchase order acknowledged successfully."}, status=status.HTTP_200_OK)
