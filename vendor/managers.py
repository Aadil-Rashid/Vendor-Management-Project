from django.db import models
from django.db.models import Avg, F
from django.utils import timezone

from vendor.constants import COMPLETED


class HistoricalPerformanceManager(models.Manager):

    def update_on_time_delivery_rate_field(self, purchase_order_obj):
        from vendor.models import PurchaseOrder
        vendor = purchase_order_obj.vendor

        # Count the number of completed POs delivered on or before delivery_date
        completed_orders_count = PurchaseOrder.objects.filter(
            vendor=vendor, status=COMPLETED, acknowledgment_date__lte=purchase_order_obj.delivery_date
        ).count()

        # Count the total number of completed POs for that vendor
        total_completed_orders_count = PurchaseOrder.objects.filter(
            vendor=vendor, status=COMPLETED
        ).count()

        # Calculate on-time delivery rate
        if total_completed_orders_count > 0:
            on_time_delivery_rate = round((
                completed_orders_count / total_completed_orders_count) * 100, 2)
        else:
            on_time_delivery_rate = 0

        # Update or create HistoricalPerformance entry for the vendor
        self.update_or_create(
            vendor=vendor,
            defaults={
                'date':  timezone.now(),
                'on_time_delivery_rate': on_time_delivery_rate,
            }
        )

    def update_quality_rating_avg_field(self, purchase_order_obj):
        from vendor.models import PurchaseOrder
        vendor = purchase_order_obj.vendor

        quality_rating_avg = PurchaseOrder.objects.filter(
            vendor=vendor, status=COMPLETED
        ).aggregate(avg_rating=Avg('quality_rating'))["avg_rating"]

        self.update_or_create(
            vendor=vendor,
            defaults={
                'date':  timezone.now(),
                'quality_rating_avg': quality_rating_avg,
            }
        )

    def update_average_response_time_field(self, purchase_order_obj):
        from vendor.models import PurchaseOrder
        vendor = purchase_order_obj.vendor

        # Calculate average response time
        avg_response_time_timedelta = PurchaseOrder.objects.filter(vendor=vendor).annotate(
            time_difference=F('acknowledgment_date') - F('issue_date')
        ).aggregate(avg_time_difference=Avg('time_difference'))['avg_time_difference']

        # Extract the numeric value from the timedelta object
        avg_response_time_seconds = avg_response_time_timedelta.total_seconds()
        # Convert seconds to hours
        avg_response_time_hours = round(avg_response_time_seconds / 3600, 2)

        self.update_or_create(
            vendor=vendor,
            defaults={
                'date':  timezone.now(),
                'average_response_time': avg_response_time_hours,
            }
        )

    def update_fulfillment_rate_field(self, purchase_order_obj):
        from vendor.models import PurchaseOrder
        vendor = purchase_order_obj.vendor

        total_purchased_orders = PurchaseOrder.objects.filter(
            vendor=vendor).count()
        completed_orders_without_issues = PurchaseOrder.objects.filter(vendor=vendor, status=COMPLETED,
                                                                       acknowledgment_date__lte=purchase_order_obj.delivery_date).count()

        if total_purchased_orders > 0:
            fulfillment_rate = round(
                completed_orders_without_issues / total_purchased_orders, 2)
        else:
            fulfillment_rate = 0

        self.update_or_create(
            vendor=vendor,
            defaults={
                'date':  timezone.now(),
                'fulfillment_rate': fulfillment_rate,
            }
        )
