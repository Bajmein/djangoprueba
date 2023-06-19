from django import forms
from django.forms import ModelForm
from .models import Comentarios


class UserForm(forms.Form):
    username = forms.CharField(max_length=20, label='', widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
    password = forms.CharField(max_length=20, label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class PaisajeForm(ModelForm):
    class Meta:
        model = Comentarios
        fields = ['titulo', 'comentario']
