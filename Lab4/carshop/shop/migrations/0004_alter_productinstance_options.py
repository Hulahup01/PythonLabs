# Generated by Django 4.2.1 on 2023-06-03 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_date_created_productinstance_date_of_purchase'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productinstance',
            options={'ordering': ['price', 'product']},
        ),
    ]