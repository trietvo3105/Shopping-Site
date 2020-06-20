from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class KhachHangUser(AbstractUser):
    photo = models.ImageField(upload_to="profile/", blank=True)
    sdt = models.CharField(default='', max_length=15, null=False)
    def __str__(self):
        return self.username


class DiaChiKhachHang(models.Model):
    #id = models.BigIntegerField(primary_key=True, default=0)
    user = models.ForeignKey(KhachHangUser, on_delete=models.CASCADE)
    dia_chi = models.CharField(max_length=255, blank=True)

    # class Meta:
    #     unique_together = (('user', 'dia_chi'),)

    def __str__(self):
        return str(self.user)
