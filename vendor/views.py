from django.utils import timezone
from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from vendor.models import Vendor, PurchaseOrder, HistoricalPerformance
from vendor.serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer
from vendor.pagination import CustomPageNumberPagination
from vendor.authenticate import CustomAuthentication


class VendorListCreateAPIView(generics.ListCreateAPIView):
    authentication_classes = [CustomAuthentication]
    pagination_class = CustomPageNumberPagination
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()


class VendorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [CustomAuthentication]
    serializer_class = VendorSerializer
    queryset = Vendor.objects.all()
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        id = instance.id
        instance.delete()
        message = {
            "message": f"Vendor instance with id={id} has been deleted Successfully"}
        return Response(message, status=status.HTTP_204_NO_CONTENT)


class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    authentication_classes = [CustomAuthentication]
    serializer_class = PurchaseOrderSerializer
    pagination_class = CustomPageNumberPagination
    queryset = PurchaseOrder.objects.all()


class PurchaseOrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [CustomAuthentication]
    serializer_class = PurchaseOrderSerializer
    queryset = PurchaseOrder.objects.all()
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        id = instance.id
        instance.delete()
        message = {
            "message": f"PurchaseOrder instance with id={id} has been deleted Successfully"}
        return Response(message, status=status.HTTP_204_NO_CONTENT)


class VendorPerformanceListAPIView(generics.ListAPIView):
    authentication_classes = [CustomAuthentication]
    serializer_class = HistoricalPerformanceSerializer
    queryset = HistoricalPerformance.objects.all()
    lookup_field = 'vendor_id'

    def get_queryset(self):
        vendor_id = self.kwargs.get(self.lookup_field)

        try:
            # Retrieve the HistoricalPerformance object for the specified vendor ID
            performance = HistoricalPerformance.objects.get(
                vendor_id=vendor_id)
            return performance
        except HistoricalPerformance.DoesNotExist:
            return []

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AcknowledgmentAPIView(APIView):
    authentication_classes = [CustomAuthentication]

    def post(self, request, *args, **kwargs):
        po_id = kwargs['po_id']
        obj = get_object_or_404(PurchaseOrder, id=po_id)
        obj.acknowledgment_date = timezone.now()
        obj.save()
        message = {
            "message": "acknowledgment_date for PurchaseOrder instance Successfully updated"}
        return Response(message, status=status.HTTP_200_OK)
