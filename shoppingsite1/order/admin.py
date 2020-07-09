from django.contrib import admin
from .models import DonHang, ItemTrongDonHang

class IItemTrongDonHangAdmin(admin.TabularInline):
    model = ItemTrongDonHang

class ItemTrongDonHangAdmin(admin.ModelAdmin):
    list_display = ['don_hang', 'item']
    list_per_page = 20

class DonHangAdmin(admin.ModelAdmin):
    inlines = [IItemTrongDonHangAdmin]
    list_display = ['pk', 'user', 'cart', 'total', 'dia_chi_giao_hang', 'thoi_gian_dat_hang', 'trang_thai']
    list_display_links = ['user']
    list_filter = ['khach_hang', 'trang_thai', 'thoi_gian_dat_hang']
    list_per_page = 20
    fields = (('khach_hang', 'dia_chi_giao_hang'), 'thoi_gian_dat_hang', ('total', 'phi_ship', 'voucher'), 'trang_thai')
    actions = ("Accept_Carts", "Deny_Carts", "Cancelled_Carts", "Delivering_Carts", "Delivered_Carts")
    # search_fields = ['trang_thai']
    def user(self,obj):
        return "{}".format(obj.khach_hang)
    def pk(self,obj):
        return "{}".format(obj.pk)
    def Accept_Carts(self, request, queryset):
        count = queryset.update(trang_thai=1)
        self.message_user(request, 'Đã chấp nhận {} đơn hàng.'.format(count))
    def Deny_Carts(self, request, queryset):
        count = queryset.update(trang_thai=2)
        self.message_user(request, 'Đã từ chối {} đơn hàng.'.format(count))
    def Cancelled_Carts(self, request, queryset):
        count = queryset.update(trang_thai=3)
        self.message_user(request, 'Khách hàng đã hủy {} đơn hàng.'.format(count))
    def Delivering_Carts(self, request, queryset):
        count = queryset.update(trang_thai=4)
        self.message_user(request, 'Đang giao {} đơn hàng.'.format(count))
    def Delivered_Carts(self, request, queryset):
        count = queryset.update(trang_thai=5)
        self.message_user(request, 'Đã giao {} đơn hàng.'.format(count))


admin.site.register(DonHang, DonHangAdmin)
admin.site.register(ItemTrongDonHang, ItemTrongDonHangAdmin)
