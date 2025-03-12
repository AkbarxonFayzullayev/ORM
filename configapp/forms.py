import re

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import News, Categories

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'context', 'is_bool', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'context': forms.Textarea(attrs={'class': 'form-control', 'row': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
    }

    def clean_title(self):
        title = self.cleaned_data["title"]
        if re.match(r'\d',title):
            raise ValidationError("Title raqam bo'lmasin")
        return title

class CategoryForm(forms.Form):
    title = forms.CharField(max_length=140, label='Sarlavha kiriting ',
                            widget=forms.TextInput(attrs={"class": 'form-control'}))

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Login',widget=forms.TextInput(attrs=({'class': 'form-control'})))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs=({'class': 'form-control'})))

    class Meta:
        model = User
        fields = ('username','password')