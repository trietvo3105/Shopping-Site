# Generated by Django 3.0.7 on 2020-07-02 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0005_auto_20200702_1723'),
        ('cart_origin', '0004_auto_20200702_1744'),
    ]

    operations = [
        migrations.CreateModel(
            name='GioHang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tao_vao', models.DateTimeField()),
                ('cap_nhat_vao', models.DateTimeField(auto_now=True, verbose_name='Cập nhật vào')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItemTrongGioHang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('so_luong', models.IntegerField(default=0)),
                ('gio_hang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart_origin.GioHang')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Sach')),
            ],
        ),
    ]
