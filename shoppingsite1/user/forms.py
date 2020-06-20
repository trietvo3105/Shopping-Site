from django import forms
import re
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import KhachHangUser, DiaChiKhachHang


# class FormDangKy(forms.Form):
#     tai_khoan = forms.CharField(label='Tài khoản', max_length=30)
#     email = forms.EmailField(label='Email')
#     matkhau1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
#     matkhau2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput())
#
#     def clean_password2(self):
#         if 'matkhau1' in self.cleaned_data:
#             matkhau1 = self.cleaned_data['matkhau1']
#             matkhau2 = self.cleaned_data['matkhau2']
#             if matkhau1 == matkhau2 and matkhau1:
#                 return matkhau2
#         raise forms.ValidationError("Mật khẩu không hợp lệ")
#
#     def clean_username(self):
#         tai_khoan = self.cleaned_data['tai_khoan']
#         if not re.search(r'^\w+&', tai_khoan):
#             raise forms.ValidationError("Tên tài khoản có kí tự đặc biệt")
#         try:
#             KhachHangUser.objects.get(username=tai_khoan)
#         except KhachHangUser.DoesNotExist:
#             return tai_khoan
#         raise forms.ValidationError("Tài khoản đã tồn tại")
#
#     def save(self):
#         KhachHangUser.objects.create_user(username=self.cleaned_data['tai_khoan'], email=self.cleaned_data['email'],
#                                  password=self.cleaned_data['matkhau1'])


class FormDangKy(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email',)


class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'sdt', 'photo', 'username',)


class AddressUpdateForm(forms.ModelForm):
    class Meta:
        model = DiaChiKhachHang
        fields = ('dia_chi',)