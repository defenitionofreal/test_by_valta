# core
from apps.catalog.models import Product
from apps.catalog.serializers import (ProductSerializer,
                                      FilialPriceSerializer,
                                      CharacteristicSerializer)
# rest
from rest_framework import (permissions,
                            viewsets)
from rest_framework.decorators import action
from rest_framework.response import Response


class CatalogViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny, ]
    queryset = Product.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"filial": self.request.query_params.get('filial')})
        return context

    def get_queryset(self):
        filial_id = self.request.query_params.get("filial")
        characteristic_id = self.request.query_params.get("characteristic")
        queryset = super().get_queryset()
        if filial_id and not characteristic_id:
            queryset = Product.objects.filter(
                filial_prices__filial_id=filial_id)
            return queryset
        elif filial_id and characteristic_id:
            queryset = Product.objects.filter(
                filial_prices__filial_id=filial_id,
                characteristics__id=characteristic_id)
            return queryset
        else:
            return queryset

    @action(detail=True)
    def characteristic(self, request, pk=None):
        characteristics = self.get_object().characteristics.all()
        serializer = CharacteristicSerializer(characteristics, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def price(self, request, pk=None):
        filial_id = self.request.query_params.get("filial")
        filial_price = self.get_object().filial_prices.all()
        if filial_id:
            filial_price = self.get_object().filial_prices.filter(
                filial_id=filial_id)
        serializer = FilialPriceSerializer(filial_price, many=True)
        return Response(serializer.data)
