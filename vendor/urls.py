from django.urls import path

from vendor.views import VendorListCreateAPIView
from vendor.views import VendorRetrieveUpdateDestroyAPIView
from vendor.views import PurchaseOrderListCreateAPIView
from vendor.views import PurchaseOrderRetrieveUpdateDestroyAPIView
from vendor.views import VendorPerformanceListAPIView
from vendor.views import AcknowledgmentAPIView


urlpatterns = [
    # Vendor Profile Management: routes

    path('vendors/', VendorListCreateAPIView.as_view(),
         name="vendor_list_create_api"),

    path('vendors/<int:id>/', VendorRetrieveUpdateDestroyAPIView.as_view(),
         name='vendor_retrieve_update_destroy_api'),

    # Purchase Order Tracking: routes

    path('purchase_orders/', PurchaseOrderListCreateAPIView.as_view(),
         name="purchase_orders_list_create_api"),

    path('purchase_orders/<int:id>/', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(),
         name='purchase_orders_retrieve_update_destroy_api'),

    # Vendor Performance Evaluation: routes

    path('vendors/<int:vendor_id>/performance/', VendorPerformanceListAPIView.as_view(),
         name='vendor_performance_api'),


    # UpdateAcknowledgment:
    path('purchase_orders/<int:po_id>/acknowledge/', AcknowledgmentAPIView.as_view(),
         name='update_acknowledge_api'),
]
