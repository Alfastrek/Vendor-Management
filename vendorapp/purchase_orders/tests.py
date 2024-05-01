from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import PurchaseOrder, Vendor

class AcknowledgePurchaseOrderTests(APITestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(name='Test Vendor', contact_details='test@example.com', address='123 Test St', vendor_code='ABC123')
        self.purchase_order = PurchaseOrder.objects.create(po_number='PO123', vendor=self.vendor, order_date='2024-05-01', delivery_date='2024-05-10', items={'item': 'test'}, quantity=1, status='pending', issue_date='2024-05-01')

    def test_acknowledge_purchase_order_endpoint(self):
        url = reverse('acknowledge-purchase-order', kwargs={'pk': self.purchase_order.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.purchase_order.refresh_from_db()
        self.assertIsNotNone(self.purchase_order.acknowledgment_date)
