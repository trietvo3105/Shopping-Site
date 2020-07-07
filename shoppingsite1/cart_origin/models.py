from django.db import models
from user.models import KhachHangUser
from book.models import Sach
# Create your models here.


class GioHang(models.Model):
    user = models.ForeignKey(KhachHangUser, on_delete=models.CASCADE)
    tao_vao = models.DateTimeField()
    def __str__(self):
        return str(self.user) + '(' + str(self.pk) + ')'


# class ItemTrongGioHang(models.Model):
#     gio_hang = models.ForeignKey(GioHang, on_delete=models.CASCADE)
#     item = models.ForeignKey(Sach, on_delete=models.CASCADE)
#     so_luong = models.IntegerField(default=0)
#     def __str__(self):
#         return str(self.gio_hang) + ', ' + str(self.item)