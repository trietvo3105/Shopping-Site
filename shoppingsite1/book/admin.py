from django.contrib import admin
from .models import LoaiSach, Sach, DotNhapSach
# Register your models here.
class SachAdmin(admin.ModelAdmin):
    list_display = ['pk', 'ten', 'loai_sach', 'tac_gia', 'nxb', 'nam_xb', 'so_luong_con', 'so_luong_nhap', 'don_gia']
    list_display_links = ['ten']
    list_filter = ['loai_sach', 'nxb']
    list_per_page = 20
    search_fields = ['ten']

admin.site.register(LoaiSach)
admin.site.register(Sach, SachAdmin)
admin.site.register(DotNhapSach)