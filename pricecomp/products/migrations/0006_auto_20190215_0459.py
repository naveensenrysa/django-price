# Generated by Django 2.1.7 on 2019-02-15 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20190214_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='scrape_data',
        ),
        migrations.AddField(
            model_name='price',
            name='scrape_id',
            field=models.IntegerField(null=True),
        ),
    ]
