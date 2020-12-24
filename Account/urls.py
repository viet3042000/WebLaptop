from django.urls import path, include
from . import views
from .views import SetNewPasswordView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='store/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', SetNewPasswordView.as_view(), name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='store/password_reset_complete.html'),
         name='password_reset_complete'),

    path('resetpass/', views.send_email, name='resetpass'),
    path('register/', views.register, name='register'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('profile/', views.view_profile, name='profile'),
    path('accounts/', include('allauth.urls')),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login_view, name='login'),
]
