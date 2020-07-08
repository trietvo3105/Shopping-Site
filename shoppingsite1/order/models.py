from django.db import models
from user.models import KhachHangUser,DiaChiKhachHang
from voucher.models import Voucher
from book.models import Sach
from cart_origin.models import *
# Create your models here.
class DonHang(models.Model):
    #thoi_gian_giao_hang = models.CharField(default='', max_length=15)
    thoi_gian_dat_hang = models.DateTimeField()
    trang_thai_choice = ((0, 'Chờ duyệt...'), (1, 'Chấp nhận'), (2, 'Bị admin từ chối'), (3, 'Bị khách hàng hủy'), (4, 'Đang giao...'), (5, 'Đã giao xong!'))
    trang_thai = models.IntegerField(choices=trang_thai_choice, default=0)
    #giao_hang_choice = ((0, 'Giao hàng nhanh'), (1, 'Giao hàng tiết kiệm'), (2, 'Bưu điện'))
    #phuong_thuc_giao_hang = models.IntegerField(choices=giao_hang_choice, default=0)
    dia_chi_giao_hang = models.ForeignKey(DiaChiKhachHang,on_delete=models.CASCADE)
    phi_ship = models.IntegerField(default=12)
    khach_hang = models.ForeignKey(KhachHangUser, on_delete=models.CASCADE)
    cart = models.ForeignKey(GioHang, on_delete=models.CASCADE)
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE, null=True)
    total = models.IntegerField(default=10)
    # tao_vao = models.DateTimeField('Tạo vào', auto_now_add=True)
    #items = models.ForeignKey(ItemTrongGioHang, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.khach_hang) + ' (' + str(self.pk)+ ')'


# class XuLyDonHang(models.Model):
#     admin = models.ForeignKey(KhachHangUser, on_delete=models.CASCADE, primary_key=True)
#     id_don_hang = models.ForeignKey(DonHang, on_delete=models.CASCADE, primary_key=True)


# class GhiChu(models.Model):
#     admin = models.ForeignKey(XuLyDonHang.admin, on_delete=models.CASCADE, primary_key=True)
#     id_don_hang = models.ForeignKey(XuLyDonHang.id_don_hang, on_delete=models.CASCADE, primary_key=True)
#     [admin, id_don_hang] = models.ForeignKey(XuLyDonHang, on_delete=models.CASCADE)
#     noi_dung = models.TextField(primary_key=True)
#     ngay = models.CharField(primary_key=True)
#     gio = models.CharField(primary_key=True)
class ItemTrongDonHang(models.Model):
    don_hang = models.ForeignKey(DonHang, on_delete=models.CASCADE)
    item = models.ForeignKey(Sach, on_delete=models.CASCADE)
    so_luong = models.IntegerField()
    def __str__(self):
        return str(self.don_hang) + ', ' + str(self.item)