# Generated by Django 2.1.7 on 2019-02-14 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20190214_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scrape',
            name='ndh_pk',
        ),
        migrations.AlterField(
            model_name='scrape',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Productsndh'),
        ),
    ]
