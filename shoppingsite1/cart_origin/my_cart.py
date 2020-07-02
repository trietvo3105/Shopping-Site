from cart.cart import Cart
from book.models import Sach
from decimal import Decimal
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

class MyCart(Cart):
    # def not_correct(self, request):
    #     return messages.warning(request, 'Số lượng sản phẩm')

    def add(self, product, quantity=1, action=None):
        """
        Add a product to the cart or update its quantity.
        """
        id = product.id
        newItem = True
        if str(product.id) not in self.cart.keys():

            self.cart[product.id] = {
                'userid': self.request.user.id,
                'product_id': id,
                'name': product.ten,
                'quantity': 1,
                'so_luong_con': product.so_luong_con-1,
                'so_luong_nhap': product.so_luong_nhap,
                'price': str(product.don_gia),
                'image': product.hinh_anh.url
            }

        else:
            newItem = True

            for key, value in self.cart.items():
                if key == str(product.id):
                    if (value['so_luong_con'] < 1):
                        print("Not correct")
                        print(value['quantity'])
                        print(value['so_luong_con'])
                        value['quantity'] = value['quantity']
                    else:
                        print(value['quantity'])
                        print(value['so_luong_con'])
                        value['quantity'] = value['quantity'] + 1
                        value['so_luong_con'] = value['so_luong_con'] - 1
                    newItem = False
                    self.save()
                    break
            if newItem == True:

                self.cart[product.id] = {
                    'userid': self.request,
                    'product_id': product.id,
                    'name': product.ten,
                    'quantity': 1,
                    'so_luong_con': product.so_luong_con - 1,
                    'so_luong_nhap': product.so_luong_nhap,
                    'price': str(product.don_gia),
                    'image': product.hinh_anh.url
                }

        self.save()

    def decrement(self, product):
        for key, value in self.cart.items():
            if key == str(product.id):
                value['quantity'] = value['quantity'] - 1
                value['so_luong_con'] = value['so_luong_con'] + 1
                if (value['quantity'] < 1):
                    return redirect('cart:cart_detail')
                self.save()
                break
            else:
                print("Something Wrong")

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Sach.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
