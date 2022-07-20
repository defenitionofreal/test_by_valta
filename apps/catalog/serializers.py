from rest_framework import serializers
from apps.catalog.models import Product, Filial, FilialPrice, Characteristic


class ProductSerializer(serializers.ModelSerializer):
    """
    Price field is designed to search for a price from a specific affiliate.
    """

    price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ("id", "name", "price")

    def get_price(self, obj):
        filial = self.context["filial"]
        price_by_filial = obj.filial_prices.values_list("price", flat=True) \
            .filter(filial_id=filial).first()
        return price_by_filial

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class FilialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filial
        fields = ("id", "name", "region")

    def create(self, validated_data):
        return Filial.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.name = validated_data.get("region", instance.region)
        instance.save()
        return instance


class FilialPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilialPrice
        fields = ("id", "product", "filial", "price")

    def create(self, validated_data):
        return FilialPrice.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("product", instance.product)
        instance.name = validated_data.get("filial", instance.filial)
        instance.name = validated_data.get("price", instance.price)
        instance.save()
        return instance


class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = ("id", "self", "name", "product_id")

    def create(self, validated_data):
        return Characteristic.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("self", instance.self)
        instance.name = validated_data.get("name", instance.name)
        instance.name = validated_data.get("product_id", instance.product_id)
        instance.save()
        return instance
