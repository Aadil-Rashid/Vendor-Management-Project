from django.conf import settings

from rest_framework import serializers

from vendor.models import Vendor, PurchaseOrder, HistoricalPerformance


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"


class CustomDateTimeField(serializers.DateTimeField):
    def to_representation(self, value):
        if value is None:
            return None
        return value.strftime(settings.LISTING_DATE_FORMAT)


class PurchaseOrderSerializer(serializers.ModelSerializer):
    order_date = CustomDateTimeField(required=False)
    delivery_date = CustomDateTimeField()
    issue_date = CustomDateTimeField()
    acknowledgment_date = CustomDateTimeField(required=False)

    class Meta:
        model = PurchaseOrder
        fields = "__all__"


class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        exclude = ["id", "vendor", "date"]
