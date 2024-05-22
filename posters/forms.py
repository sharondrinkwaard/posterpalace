from django import forms
from .models import Poster


class PosterColor(forms.ModelForm):
    class Meta:
        model = Poster
        fields = ('color_option',)


class PosterQuantity(forms.ModelForm):
    class Meta:
        model = Poster
        fields = ('quantity',)