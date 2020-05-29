from django.db import models
from datetime import date
# Create your models here.
class LoaiSach(models.Model):
    ten = models.CharField(default='', max_length=255)
    slug = models.SlugField(max_length=254, unique=True, blank=True, editable=True)
    def __str__(self):
        return self.ten


class Sach(models.Model):
    ten = models.CharField(default='', max_length=255)
    tac_gia = models.CharField(default='', max_length=255)
    nxb = models.CharField(default='', max_length=255)
    nam_xb = models.IntegerField(default=0)
    mo_ta = models.TextField(default='')
    upload_to = 'img/news/{0}/{1}'.format(date.today().year, date.today().month)
    hinh_anh = models.ImageField(upload_to=upload_to, blank=True, null=True, max_length=254, verbose_name=('Ảnh bìa'))
    so_luong_con = models.IntegerField(default=0)
    so_luong_nhap = models.IntegerField(default=0)
    don_gia = models.IntegerField(default=0)
    loai_sach = models.ForeignKey(LoaiSach, on_delete=models.CASCADE)
    def __str__(self):
        return self.ten


class DotNhapSach(models.Model):
    id_sach = models.ForeignKey(Sach, on_delete=models.CASCADE, primary_key=True)
    ngay_nhap = models.CharField(max_length=15)
    so_luong = models.IntegerField(default=0)
    gia_nhap = models.IntegerField(default=0)

    class Meta:
        unique_together = (('id_sach', 'ngay_nhap'),)

    def __str__(self):
        return self.ngay_nhap

