# Generated by Django 4.1.7 on 2023-04-12 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_orders_razor_pay_order_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='razor_pay_order_id',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='razor_pay_payment_id',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='razor_pay_payment_signature',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='razor_pay_order_id',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='razor_pay_payment_id',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='razor_pay_payment_signature',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]