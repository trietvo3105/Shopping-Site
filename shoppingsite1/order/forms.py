from django import forms
from .models import KhachHangUser, Sach

class Order(forms.Form):
    class Meta:
        model = Sach
        fields = ['so_luong_con']