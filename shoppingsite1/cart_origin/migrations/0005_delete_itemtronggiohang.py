# Generated by Django 3.0.7 on 2020-07-02 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_auto_20200702_2136'),
        ('cart_origin', '0004_auto_20200702_2136'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ItemTrongGioHang',
        ),
    ]