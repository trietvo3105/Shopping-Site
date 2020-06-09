from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from user.forms import FormDangKy, CustomUserUpdateForm, AddressUpdateForm
from user.models import DiaChiKhachHang
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.


class DangNhap(View):
    def get(self, request):
        return render(request, 'login/login.html')

    def post(self, request):
        tai_khoan = request.POST.get('taikhoan')
        mat_khau = request.POST.get('matkhau')
        user = authenticate(username=tai_khoan, password=mat_khau)
        if user is None:
            return HttpResponse('Tài khoản không tồn tại!')
        else:
            login(request, user)
            return render(request, 'homepage/index.html')


class UserView(LoginRequiredMixin, View):
    login_url = '/login'

    def get(self, request):
        return HttpResponse('Đây là view sau khi đăng nhập')

    def post(self):
        pass


# def dang_ky(request):
#     form = FormDangKy()
#     if request.method == 'POST':
#         form = FormDangKy(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Bạn tạo tài khoản thành công')
#     return render(request, 'login/register.html', {'form': form})


def dang_ky(request):
    if request.method == "POST":
        form = FormDangKy(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:login')
    else:
        form = FormDangKy()

    return render(request, 'login/register.html', {'form': form})



class HomePage(View):
    def get(self, request):
        return render(request, 'homepage/index.html')


@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance=user, files=request.FILES)
        a_form = [AddressUpdateForm(request.POST, prefix=str(x), instance=DiaChiKhachHang()) for x in range(0,3)]
        if form.is_valid() and all([a_f.is_valid() for a_f in a_form]):
            new_form = form.save()
            for a_f in a_form:
                new_address = a_f.save(commit=False)
                new_address.user = new_form
                new_address.save()
    else:
        form = CustomUserUpdateForm(instance=user)
        a_form = [AddressUpdateForm(prefix=str(x), instance=DiaChiKhachHang()) for x in range(0,3)]
    return render(request, 'login/profile.html', {'form': form, 'address': a_form})


@login_required
def password_change(request):
    pass