from django import forms
from crud.models import Usuario
    

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
