# Generated by Django 3.0.7 on 2020-07-02 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart_origin', '0003_auto_20200702_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemtronggiohang',
            name='gio_hang',
        ),
        migrations.RemoveField(
            model_name='itemtronggiohang',
            name='item',
        ),
        migrations.RemoveField(
            model_name='giohang',
            name='cap_nhat_vao',
        ),
    ]
