from django.urls import path
from .views import DangNhap, UserView, dang_ky, HomePage
from django.contrib.auth import views as auth_views

app_name = 'core'
urlpatterns = [
    path('login/', DangNhap.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login/logout.html'), name='logout'),
    path('register/', dang_ky, name='register'),
    path('userview/', UserView.as_view(), name='user-view'),
    path('', HomePage.as_view(), name='index'),
]