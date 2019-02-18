from django.contrib import admin

from products.models import Product, Scrape, Price
# Register your models here.
admin.site.register(Product)
admin.site.register(Scrape)
admin.site.register(Price)


