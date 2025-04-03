from django import forms

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    class Meta:
        model=User
        fields={'username', 'password'}

    username=forms.CharField()
    password=forms.CharField(

    )
    #username=forms.CharField(
     #   label='Имя пользователя',
      #  widget=forms.TextInput(attrs={"autofocus": True,
      #                                'class':'form-control',
       #                               'placeholder':'Введите ваше имя пользователя'}))
    #password=forms.CharField(
     #   label='Пароль',
      #  widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
       #                                 'class':'form-control',
        #                                'placeholder':'Введите ваш пароль'})
    #)
    
class UserRegistrarionForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

username = forms.CharField()
email = forms.CharField()
password1 = forms.CharField()
password2 = forms.CharField()    


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields=(
            "image",
            "username",
            "email",)
        
image = forms.ImageField(required=False)
username = forms.CharField()
email = forms.CharField()
