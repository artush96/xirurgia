from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import *


class ReviewCreateForm(forms.ModelForm):
    # content = forms.CharField(widget=CKEditorWidget(attrs={'placeholder': '* Ակնարկ'}))

    class Meta:
        model = Review
        fields = ['name_hy', 'disease_hy', 'content_hy', 'name_ru', 'disease_ru', 'content_ru', 'name_en', 'disease_en',
                  'content_en']
        exclude = ['published', 'pub_date']
        widgets = {
            'name_hy': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Անուն Ազգանուն', 'required': ''}),
            'name_ru': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Имя Фамилия', 'required': ''}),
            'name_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* First name Last name', 'required': ''}),
            'disease_hy': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Բուժված հիվանդությունը', 'required': ''}),
            'disease_ru': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Вылеченная болезнь', 'required': ''}),
            'disease_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* The cured disease', 'required': ''}),
            'content_hy': forms.Textarea(attrs={'class': 'form-control', 'rows': '6', 'placeholder': '* Ակնարկ'}),
            'content_ru': forms.Textarea(attrs={'class': 'form-control', 'rows': '6', 'placeholder': '* Коментария'}),
            'content_en': forms.Textarea(attrs={'class': 'form-control', 'rows': '6', 'placeholder': '* Comment'}),
        }
