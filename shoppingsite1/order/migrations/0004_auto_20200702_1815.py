# Generated by Django 3.0.7 on 2020-07-02 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart_origin', '0005_giohang_itemtronggiohang'),
        ('order', '0003_auto_20200702_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='donhang',
            name='cart',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cart_origin.GioHang'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donhang',
            name='items',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cart_origin.ItemTrongGioHang'),
        ),
    ]
