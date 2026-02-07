from django import forms
class LoginForm(forms.Form):
    username = forms.CharField(label="Ваше имя пользователя:")
    password = forms.CharField(label="Ваш пароль:",
                               widget = forms.PasswordInput)
class RegistrationForm(forms.Form):
   username = forms.CharField(label='Ваше имя пользователя:')
   email = forms.EmailField(label='E-mail')
   password = forms.CharField(label='Ваш пароль:', widget=forms.PasswordInput)
   password2 = forms.CharField(label='Ваш пароль повторно:', widget=forms.PasswordInput)