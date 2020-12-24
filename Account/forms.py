from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.models import User
import re

from Account.models import Customer


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(label='Email :')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError("Email đã tồn tại ")


class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


class ResetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='Mật khẩu mới', widget=forms.PasswordInput())
    new_password2 = forms.CharField(label='Nhập lại mật khẩu mới', widget=forms.PasswordInput())

    new_password1.widget.attrs.update(size='50', placeholder="Nhập mật khẩu mới")
    new_password2.widget.attrs.update(size='50', placeholder="Nhập lại mật khẩu mới")

    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']


class Profile(forms.Form):
    class Meta:
        model = Customer
        fields = ['__all__']
