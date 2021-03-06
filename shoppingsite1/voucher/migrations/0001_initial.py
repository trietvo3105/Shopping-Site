# Generated by Django 3.0.6 on 2020-05-29 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tieu_de', models.CharField(default='', max_length=255)),
                ('loai_voucher', models.IntegerField(choices=[(0, 'Trừ theo %'), (1, 'Trừ thẳng tiền')], default=0)),
                ('gia_tri', models.IntegerField(default=0)),
                ('noi_dung', models.TextField(default='', max_length=255)),
                ('ngay_bat_dau', models.CharField(default='', max_length=15)),
                ('ngay_het_han', models.CharField(default='', max_length=15)),
                ('anh_minh_hoa', models.CharField(default='', max_length=255)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
