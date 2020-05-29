from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class KhachHangUser(AbstractUser):
    avatar = models.CharField(default='', max_length=255)
    sdt = models.CharField(default='', max_length=15, null=False)
    def __str__(self):
        return self.username


class DiaChiKhachHang(models.Model):
    user = models.ForeignKey(KhachHangUser, on_delete=models.CASCADE, primary_key=True)
    dia_chi = models.CharField(max_length=255)

    class Meta:
        unique_together = (('user', 'dia_chi'),)

    def __str__(self):
        return self.user
