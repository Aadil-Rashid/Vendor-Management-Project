from django.db import models
from django.db import transaction
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator

from vendor.constants import STATUS_CHOICES, PENDING, COMPLETED
from vendor.managers import HistoricalPerformanceManager


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    vendor_code = models.CharField(max_length=255, unique=True)
    contact_details = models.TextField()
    address = models.TextField()
    on_time_delivery_rate = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)])

    def __str__(self):
        return f"{self.name} ({self.vendor_code})"


class PurchaseOrder(models.Model):

    po_number = models.CharField(max_length=255, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=9,
                              choices=STATUS_CHOICES,
                              default=PENDING,)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"PO-{self.po_number}"


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)], null=True, blank=True)
    quality_rating_avg = models.FloatField(null=True, blank=True)
    average_response_time = models.FloatField(null=True, blank=True)
    fulfillment_rate = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)], null=True, blank=True)
    objects = HistoricalPerformanceManager()

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"


# signals

@receiver(post_save, sender=PurchaseOrder)
def update_historical_performance(sender, instance, created, **kwargs):

    with transaction.atomic():
        if instance.status == COMPLETED:
            HistoricalPerformance.objects.update_on_time_delivery_rate_field(
                instance)
        if instance.quality_rating:
            HistoricalPerformance.objects.update_quality_rating_avg_field(
                instance)
        if instance.acknowledgment_date:
            HistoricalPerformance.objects.update_average_response_time_field(
                instance)


@receiver(pre_save, sender=PurchaseOrder)
def pre_save_purchase_order(sender, instance, **kwargs):

    with transaction.atomic():
        old_instance = PurchaseOrder.objects.filter(id=instance.id).first()

        if old_instance and old_instance.status != instance.status:
            HistoricalPerformance.objects.update_fulfillment_rate_field(
                instance)
