from django import forms

""" aqui se esta creando el formulario """
from.models import BDprincipal

class PrincipalForm(forms.ModelForm):
    class Meta:
        model = BDprincipal
        fields = ('__all__')