# Generated by Django 3.1.3 on 2020-12-20 16:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ('Checkout', '0005_auto_20201218_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_product',
            name='date_order',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]