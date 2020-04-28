from django import forms

from .models import DatosB

class DatosForm(forms.ModelForm):

    class Meta:
        model = DatosB
        fields = ('title', 'text',)
