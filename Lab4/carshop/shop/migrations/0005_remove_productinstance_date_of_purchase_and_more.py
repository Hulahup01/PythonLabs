# Generated by Django 4.2.1 on 2023-06-04 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_productinstance_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinstance',
            name='date_of_purchase',
        ),
        migrations.AddField(
            model_name='productinstance',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
