from django import forms
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class RegisterForm(forms.ModelForm):
    password_confirmation = forms.CharField(
        label='повтор пароля'.capitalize(), max_length=128)

    class Meta:
        model = UserModel
        fields = ('username', 'password')
        # widgets = {
        #     'password': forms.PasswordInput(),
        #     'password_confirmation': forms.PasswordInput(),
        #     }

    def clean(self):
        data = self.cleaned_data
        if data['password'] != data['password_confirmation']:
            raise forms.ValidationError('Пароли не совпадают!')
        return data
