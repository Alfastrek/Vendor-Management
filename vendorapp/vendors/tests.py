from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Vendor

class VendorPerformanceTests(APITestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(name='Test Vendor', contact_details='test@example.com', address='123 Test St', vendor_code='ABC123')

    def test_vendor_performance_endpoint(self):
        url = reverse('vendor-performance', kwargs={'pk': self.vendor.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['on_time_delivery_rate'], self.vendor.on_time_delivery_rate)
        self.assertEqual(response.data['quality_rating_avg'], self.vendor.quality_rating_avg)
        self.assertEqual(response.data['average_response_time'], self.vendor.average_response_time)
        self.assertEqual(response.data['fulfillment_rate'], self.vendor.fulfillment_rate)
