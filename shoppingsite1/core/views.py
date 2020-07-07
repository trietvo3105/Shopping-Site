from django.shortcuts import render, redirect
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from user.forms import FormDangKy, CustomUserUpdateForm, AddressUpdateForm
from user.models import DiaChiKhachHang
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from book.models import *
from voucher.models import Voucher
from cart_origin.my_cart import MyCart
from cart_origin.models import *
from order.models import *
from order.forms import Order
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
        Tn_items = Sach.objects.filter(loai_sach="3").order_by("-pk")[:6]
        Kh_items = Sach.objects.filter(loai_sach="4").order_by("-pk")[:6]
        Vh_items = Sach.objects.filter(loai_sach="1").order_by("-pk")[:6]
        Nt_items = Sach.objects.filter(loai_sach="2").order_by("-pk")[:6]
        Nv_items = Sach.objects.filter(loai_sach="5").order_by("-pk")[:6]
        context = {
            'Tn_items': Tn_items,
            'Kh_items': Kh_items,
            'Vh_items': Vh_items,
            'Nt_items': Nt_items,
            'Nv_items': Nv_items,
        }
        return render(request, 'homepage/index.html', context)
    def post(self, request):
        pass

class ThieuNhi(View):
    def __init__(self, **kwargs):
        super(**kwargs)
        self.loai_sach = "3"
        self.link = 'thieunhi/thieunhi.html'
    def get(self, request):
        posts = Sach.objects.filter(loai_sach=self.loai_sach).order_by("-pk")
        paginator = Paginator(posts, 9)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        return render(request, self.link, {'posts': posts})

class KhoaHoc(ThieuNhi):
    def __init__(self, **kwargs):
        super(**kwargs)
        self.loai_sach = "4"
        self.link = 'khoahoc/khoahoc.html'

class NgoaiVan(ThieuNhi):
    def __init__(self, **kwargs):
        super(**kwargs)
        self.loai_sach = "5"
        self.link = 'ngoaivan/ngoaivan.html'


class VanHoc(ThieuNhi):
    def __init__(self, **kwargs):
        super(**kwargs)
        self.loai_sach = "1"
        self.link = 'vanhoc/vanhoc.html'


class NgheThuat(ThieuNhi):
    def __init__(self, **kwargs):
        super(**kwargs)
        self.loai_sach = "2"
        self.link = 'nghethuat/nghethuat.html'



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
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('core:profile'))
        else:
            return redirect(reverse('core:password_change'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'login/password_change.html', args)


@login_required(login_url='/login/')
def cart_add(request, id):
    cart = MyCart(request)
    product = Sach.objects.get(id=id)
    cart.add(product=product)
    return redirect('core:index')


@login_required(login_url='/login/')
def cart_clear(request):
    cart = MyCart(request)
    cart.clear()
    return redirect('core:cart_detail')


@login_required(login_url='/login/')
def cart_detail(request):
    now = timezone.now()
    voucher = Voucher.objects.filter(ngay_bat_dau__lte=now, ngay_het_han__gte=now)
    # voucher = Voucher.objects.all
    dia_chi = DiaChiKhachHang.objects.filter(user=request.user).order_by("-pk")[:3]
    return render(request, 'cart/cart_detail.html', {'voucher':voucher,'dia_chi':dia_chi})


@login_required(login_url='/login/')
def item_clear(request, id):
    cart = MyCart(request)
    product = Sach.objects.get(id=id)
    cart.remove(product)
    return redirect('core:cart_detail')


@login_required(login_url='/login/')
def item_increment(request, id):
    cart = MyCart(request)
    product = Sach.objects.get(id=id)
    cart.add(product=product)
    return redirect('core:cart_detail')


@login_required(login_url='/login/')
def item_decrement(request, id):
    cart = MyCart(request)
    product = Sach.objects.get(id=id)
    cart.decrement(product=product)
    return redirect('core:cart_detail')


@login_required(login_url='/login/')
def cart_final_value(request):
    global voucher_used, shipping_cost, dia_chi_id, total
    now = timezone.now()
    dia_chi = DiaChiKhachHang.objects.filter(user=request.user).order_by("-pk")[:3]
    #dia_chi_chon = None
    dia_chi_id = request.POST['dia_chi_id']
    dia_chi_chon = DiaChiKhachHang.objects.filter(pk=dia_chi_id).first()
    voucher = Voucher.objects.filter(ngay_bat_dau__lte=now, ngay_het_han__gte=now)
    try:
        voucher_id = request.POST['voucher_id']
        if voucher_id == '':
            voucher_id = 0
        voucher_used = Voucher.objects.get(id=voucher_id,ngay_bat_dau__lte=now, ngay_het_han__gte=now)
        discount = voucher_used.gia_tri
    except Voucher.DoesNotExist:
        voucher_id = ''
        discount = 0
        voucher_used = None
    cart = MyCart(request)
    #voucher = Voucher.objects.all
    subtotal = 0
    for key, value in cart.cart.items():
        subtotal += int(value['quantity']) * int(value['price'])
    shipping_cost = 10 + int(subtotal*5/100)
    total = subtotal + shipping_cost - discount
    if total <0:
        total = 0
    context = {'subtotal':subtotal, 'ship':shipping_cost,
               'voucher':voucher, 'discount':discount,
               'total':total, 'voucher_id':voucher_id,'dia_chi':dia_chi,'dia_chi_id':dia_chi_id,'dia_chi_chon':dia_chi_chon}
    return render(request, 'cart/cart_detail.html', context)


@login_required(login_url='/login/')
def voucher_display(request):
    now = timezone.now()
    voucher = Voucher.objects.filter(ngay_bat_dau__lte=now,ngay_het_han__gte=now)
    # voucher = Voucher.objects.all
    #dia_chi = DiaChiKhachHang.objects.filter(user=request.user).order_by("-pk")[:3]
    return render(request, 'cart/cart_detail.html', {'voucher':voucher})


@login_required(login_url='/login/')
def don_hang(request):
    cart = MyCart(request)
    gio_hang = GioHang.objects.create(user=request.user, tao_vao=timezone.now())
    gio_hang.save()
    dia_chi = DiaChiKhachHang.objects.filter(pk=dia_chi_id).first()
    donhang = DonHang.objects.create(khach_hang=request.user, cart=gio_hang, voucher=voucher_used,
                                     thoi_gian_dat_hang=timezone.now(), dia_chi_giao_hang=dia_chi,
                                     phi_ship=shipping_cost, total=total)
    donhang.save()
    for product in cart:
        remain_item = Sach.objects.get(pk=product['product_id'])
        remain_item.so_luong_con = product['so_luong_con']
        remain_item.save()
        order_item = Sach.objects.get(pk=product['product_id'])
        order_item = ItemTrongDonHang.objects.create(don_hang=donhang, item=order_item, so_luong=product['quantity'])
        order_item.save()
    cart.clear()
    return redirect('core:order_detail', id=donhang.pk)

@login_required(login_url='/login/')
def don_hang_detail(request, id):
    user = request.user
    target_order = DonHang.objects.get(pk=id, khach_hang=user)
    context = {'user':user, 'order':target_order}
    return render(request, 'order/order_detail.html', context)

@login_required(login_url='/login/')
def don_hang_list(request):
    order_list = DonHang.objects.filter(khach_hang=request.user).order_by("-pk")
    return render(request,'order/order_user_list.html', {'order_list':order_list})