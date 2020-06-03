from django.urls import path
from .views import DangNhap, UserView, dang_ky
from . import views

app_name = 'core'
urlpatterns = [
    path('login/', DangNhap.as_view(), name='login'),
    path('register/', dang_ky, name='register'),
    path('userview/', UserView.as_view(), name='user-view'),
    path('profile/', views.profile, name='profile'),
]