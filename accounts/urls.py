from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register', views.registerPage, name='register'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('', views.home, name='home'),
    path('user', views.userPage, name='user'),
    path('user/profile', views.profile, name='profile'),
    path('products/', views.products, name='products'),
    path('customer/<int:pk>/', views.customer, name='customer'),
    path('create-order/<int:pk>', views.createOrder, name='create-order'),
    path('update-order/<int:pk>', views.updateOrder, name='update-order'),
    path('delete-order/<int:pk>', views.deleteOrder, name='delete-order'),
    path('reset-password', auth_views.PasswordResetView.as_view(template_name='accounts/reset-password.html'), name='reset_password'),
    path('reset-password-sent', auth_views.PasswordResetDoneView.as_view(template_name='accounts/reset-password-sent.html'), name='password_reset_done'),
    path('reset-password/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/reset-password-form.html'), name='password_reset_confirm'),
    path('reset-password-complete', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/reset-password-done.html'), name='password_reset_complete'),
]
