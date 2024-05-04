from django import forms
from .models import Poster


class ProductColor(forms.ModelForm):
    class Meta:
        model = Poster
        fields = ('color_option',)