from django import forms

class contactoForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    email=forms.EmailField(max_length=60)
    texto = forms.CharField(widget=forms.Textarea)