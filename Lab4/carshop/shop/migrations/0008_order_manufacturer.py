# Generated by Django 4.2.1 on 2023-06-04 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_remove_product_manufacturer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='manufacturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.manufacturer'),
        ),
    ]