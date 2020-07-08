from django.contrib import admin
from .models import KhachHangUser, DiaChiKhachHang
# Register your models here.
class DiaChiKhachHangAdmin(admin.ModelAdmin):
    list_display = ['user', 'dia_chi']
    list_display_links = ['user']
    list_filter = ['user']
    list_per_page = 20


admin.site.register(KhachHangUser)
admin.site.register(DiaChiKhachHang, DiaChiKhachHangAdmin)
