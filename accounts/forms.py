from django import forms

from .models import Accessor

class AccessorForm(forms.ModelForm):

    class Meta:
        model = Accessor
        fields = ('username', 'password',)