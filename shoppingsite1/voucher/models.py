from django.db import models
from user.models import KhachHangUser
# Create your models here.


class Voucher(models.Model):
    tieu_de = models.CharField(default='', max_length=255)
    loai_voucher_choice = ((0, 'Trừ theo %'), (1, 'Trừ thẳng tiền'))
    loai_voucher = models.IntegerField(choices=loai_voucher_choice, default=0)
    gia_tri = models.IntegerField(default=0)
    noi_dung = models.TextField(default='', max_length=255)
    ngay_bat_dau = models.CharField(default='', max_length=15)
    ngay_het_han = models.CharField(default='', max_length=15)
    anh_minh_hoa = models.CharField(default='', max_length=255)
    admin = models.ForeignKey(KhachHangUser, on_delete=models.CASCADE)
    def __str__(self):
        return self.tieu_de
