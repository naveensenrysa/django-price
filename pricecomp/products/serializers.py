from rest_framework import serializers

from products.models import *


class PriceSerializer(serializers.ModelSerializer):
    # pk = serializers.IntegerField(required=False)

    class Meta:
        model = Price
        fields = '__all__'
        # fields = [
        #     "pk",
        #     "marketplace",
        #     "price",
        #     "updated_at",
        # ]

        # depth = 2

class ScrapeSerializer(serializers.ModelSerializer):
    # prices = PriceSerializer(many=True)
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Scrape
        fields = [
            "id",
            "marketplace_type",
            "url",
            "is_active",
        ]
class ScrapePriceSerializer(serializers.ModelSerializer):
    prices = PriceSerializer(many=True)
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Scrape
        fields = [
            "id",
            "marketplace_type",
            "url",
            "is_active",
            "created_at",
            "updated_at",
            "prices"
        ]

class ScrapePostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Scrape
        fields = [
            "id",
            "marketplace_type",
            "url",
            "is_active",
            "product"
        ]

class ProductSerializer(serializers.ModelSerializer):
    # scrapes = ScrapeSerializer(many=True)
    # prices = PriceSerializer(many=True)
    class Meta:
        model = Product
        # fields = '__all__'
        fields = [
            "ndh_id",
            "name",
            "price",
            "special_price",
            "thumbnail",
        ]



class MarketplaceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketplaceType
        fields = '__all__'


class ProductNDHSerializer(serializers.ModelSerializer):
    scrapes = ScrapeSerializer(many=True)

    class Meta:
        model = Productsndh
        fields = [
            "id",
            "name",
            "price",
            "special_price",
            "thumbnail",
            "sku",
            "scrapes"
        ]

    def update(self, instance, validated_data):
        print(validated_data)
        print('instance',instance)
        scrapes = validated_data.pop('scrapes')
        instance.name = validated_data.get("name", instance.name)
        instance.price = validated_data.get("price", instance.price)
        instance.special_price = validated_data.get("special_price", instance.special_price)
        instance.thumbnail = validated_data.get("thumbnail", instance.thumbnail)
        instance.sku= validated_data.get("sku", instance.sku)
        instance.save()
        keep_scrapes = []
        for scrape in scrapes:
            if "id" in scrape.keys():
                if Scrape.objects.filter(id=scrape["id"]).exists():
                    c = Scrape.objects.get(id=scrape["id"])
                    c.marketplace_type = scrape.get('marketplace_type', c.marketplace_type)
                    c.url = scrape.get('url', c.url)
                    c.is_active = scrape.get('is_active', c.is_active)
                    c.save()
                    keep_scrapes.append(c.id)
                else:
                    continue
            else:
                c = Scrape.objects.create(**scrape, product=instance)
                keep_scrapes.append(c.id)

        for scrape in instance.scrapes:
            if scrape.id not in keep_scrapes:
                scrape.delete()

        return instance
