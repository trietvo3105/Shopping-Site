# Generated by Django 3.0.7 on 2020-07-02 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200609_1743'),
        ('order', '0010_auto_20200702_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donhang',
            name='dia_chi_giao_hang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.DiaChiKhachHang'),
        ),
    ]
