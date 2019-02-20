from django.db import models

# Create your models here.
class Productsndh(models.Model):
    dbid = models.BigIntegerField()
    magento_id = models.IntegerField()
    sku = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    special_price = models.FloatField(blank=True, null=True)
    special_from_date = models.CharField(max_length=255, blank=True, null=True)
    special_to_date = models.CharField(max_length=255, blank=True, null=True)
    msrp = models.FloatField()
    weight = models.IntegerField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    is_in_stock = models.IntegerField()
    min_qty = models.IntegerField(blank=True, null=True)
    min_sale_qty = models.IntegerField(blank=True, null=True)
    max_sale_qty = models.IntegerField(blank=True, null=True)
    image_label = models.CharField(max_length=255, blank=True, null=True)
    image_disabled = models.IntegerField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    small_image = models.CharField(max_length=255, blank=True, null=True)
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    swatch_image = models.CharField(max_length=255, blank=True, null=True)
    product_detail_attributes = models.TextField()
    product_delivery_attributes = models.TextField()
    product_images = models.TextField()
    configurable_product_ids = models.TextField()
    configurable_product_skus = models.TextField()
    configurable_product_options = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    category_magento_ids = models.TextField(blank=True, null=True)
    brand = models.CharField(max_length=255, blank=True, null=True)
    ndh_promised = models.IntegerField(blank=True, null=True)
    popular = models.IntegerField(blank=True, null=True)
    trending = models.IntegerField(blank=True, null=True)
    visibility = models.IntegerField(blank=True, null=True)
    product_type = models.CharField(max_length=255, blank=True, null=True)
    price_range = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'productsndh'

    @property
    def scrapes(self):
        return self.scrape_set.all()


class Product(models.Model):
    ndh_id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    price = models.FloatField()
    special_price = models.FloatField()
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    sku = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def scrapes(self):
        return self.scrape_set.all()



class MarketplaceType(models.Model):
    marketplace_name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Scrape(models.Model):
    marketplace_type = models.IntegerField()
    url = models.URLField(max_length=100)
    is_active = models.BooleanField(default=True)
    product = models.ForeignKey('products.Productsndh', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def prices(self):
        return self.price_set.all()


   
class Price(models.Model):
    # scrape_id = models.IntegerField(null=True)
    scrape_data =  models.ForeignKey('products.Scrape', on_delete=models.CASCADE, blank=True, null=True)
    support_url = models.URLField(max_length=100)
    price_data = models.FloatField()
    ndh_price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)