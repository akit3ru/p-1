from django import forms
from .models import Advert
from django.forms import ModelForm
from django.core import validators
from django.forms import CharField


class SlugField(CharField):
    default_validators = [validators.validate_slug]


class AdvertForm(ModelForm):
    class Meta:
        model = Advert
        fields = ['title', 'description', 'price', 'image', 'auction']
        widgets = {'title': forms.SlugField(attrs={'class': 'form-control form-control-lg'}),
                   'description': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
                   'auction': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                   'price': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
                   'image': forms.FileInput(attrs={'class': 'form-control form-control-lg'})
                   }


form = AdvertForm()

article = Advert.objects.get(pk=1)
form = AdvertForm(instance=article)
