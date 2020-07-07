from django import forms
from user.models import KhachHangUser
from book.models import Sach

class Order(forms.Form):
    class Meta:
        model = Sach
        fields = ['so_luong_con']