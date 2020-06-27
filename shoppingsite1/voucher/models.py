from django.db import models
from user.models import KhachHangUser
from datetime import date
# Create your models here.


class Voucher(models.Model):
    tieu_de = models.CharField(default='', max_length=255)
    # loai_voucher_choice = ((0, 'Trừ theo %'), (1, 'Trừ thẳng tiền'))
    # loai_voucher = models.IntegerField(choices=loai_voucher_choice, default=0)
    gia_tri = models.IntegerField(default=0)
    noi_dung = models.TextField(default='', max_length=255)
    ngay_bat_dau = models.CharField(default='', max_length=15)
    ngay_het_han = models.CharField(default='', max_length=15)
    upload_to = 'vouchers/{0}/{1}'.format(date.today().year, date.today().month)
    image = models.ImageField(upload_to=upload_to, null=True)
    admin = models.ForeignKey(KhachHangUser, on_delete=models.CASCADE)
    def __str__(self):
        return self.tieu_de
