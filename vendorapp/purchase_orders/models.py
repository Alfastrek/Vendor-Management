from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from vendors.models import Vendor
from django.utils import timezone

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=timezone.now)
    delivery_date = models.DateTimeField(default=timezone.now)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(default=timezone.now)
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number

@receiver(post_save, sender=PurchaseOrder)
def update_on_time_delivery_rate(sender, instance, created, **kwargs):
    if instance.status == 'completed':
        completed_orders_count = sender.objects.filter(vendor=instance.vendor, status='completed').count()
        on_time_delivery_count = sender.objects.filter(vendor=instance.vendor, status='completed', delivery_date__lte=instance.delivery_date).count()
        if completed_orders_count > 0:
            instance.vendor.on_time_delivery_rate = (on_time_delivery_count / completed_orders_count) * 100
            instance.vendor.save()

@receiver(post_save, sender=PurchaseOrder)
def update_quality_rating_avg(sender, instance, created, **kwargs):
    if instance.status == 'completed' and instance.quality_rating is not None:
        completed_orders = sender.objects.filter(vendor=instance.vendor, status='completed')
        quality_rating_sum = sum(order.quality_rating for order in completed_orders if order.quality_rating is not None)
        completed_orders_count = completed_orders.count()
        if completed_orders_count > 0:
            instance.vendor.quality_rating_avg = quality_rating_sum / completed_orders_count
            instance.vendor.save()

@receiver(post_save, sender=PurchaseOrder)
def update_average_response_time(sender, instance, created, **kwargs):
    if instance.acknowledgment_date and instance.issue_date:
        response_time = instance.acknowledgment_date - instance.issue_date
        all_orders = sender.objects.filter(vendor=instance.vendor)
        total_response_time = sum((order.acknowledgment_date - order.issue_date).total_seconds() for order in all_orders if order.acknowledgment_date and order.issue_date)
        total_orders_count = all_orders.count()
        if total_orders_count > 0:
            instance.vendor.average_response_time = total_response_time / total_orders_count
            instance.vendor.save()

@receiver(post_save, sender=PurchaseOrder)
def update_fulfillment_rate(sender, instance, created, **kwargs):
    if instance.status != 'completed':
        return
    fulfilled_orders_count = sender.objects.filter(vendor=instance.vendor, status='completed').count()
    total_orders_count = sender.objects.filter(vendor=instance.vendor).count()
    if total_orders_count > 0:
        instance.vendor.fulfillment_rate = (fulfilled_orders_count / total_orders_count) * 100
        instance.vendor.save()
