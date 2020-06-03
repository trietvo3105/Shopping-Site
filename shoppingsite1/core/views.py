from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from user.forms import FormDangKy
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
            return render(request, 'login/success.html')


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