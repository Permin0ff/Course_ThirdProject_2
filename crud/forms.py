from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя", help_text="Введите свое имя", min_length=2, max_length=10)
    age = forms.IntegerField(label="Ваш возраст?", help_text="Введите свой возраст")
    reklama = forms.BooleanField(label="Coглacны получать рекламу?", required=False)
