# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AllEcommData(models.Model):
    amazon_url = models.TextField(blank=True, null=True)
    amazon_sp = models.CharField(max_length=45, blank=True, null=True)
    amazon_mrp = models.CharField(max_length=45, blank=True, null=True)
    flipkart_url = models.TextField(blank=True, null=True)
    flipkart_sp = models.CharField(max_length=45, blank=True, null=True)
    flipkart_mrp = models.CharField(max_length=45, blank=True, null=True)
    paytm_url = models.TextField(blank=True, null=True)
    paytm_sp = models.CharField(max_length=45, blank=True, null=True)
    paytm_mrp = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'all_ecomm_data'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ProductsMarketplacetype(models.Model):
    marketplace_name = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'products_marketplacetype'


class ProductsPrice(models.Model):
    support_url = models.CharField(max_length=100)
    price_data = models.FloatField()
    ndh_price = models.FloatField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    scrape_data = models.ForeignKey('ProductsScrape', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'products_price'


class ProductsProduct(models.Model):
    ndh_id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    price = models.FloatField()
    special_price = models.FloatField()
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    sku = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'products_product'


class ProductsScrape(models.Model):
    ndh_pk = models.BigIntegerField()
    marketplace_type = models.IntegerField()
    url = models.CharField(max_length=100)
    is_active = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    product = models.ForeignKey(ProductsProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'products_scrape'


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


class ScrapeData(models.Model):
    marketplace_name = models.CharField(max_length=100)
    support_url = models.CharField(max_length=200)
    is_active = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'scrape_data'
