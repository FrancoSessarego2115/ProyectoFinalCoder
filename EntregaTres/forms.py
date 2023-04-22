from django import forms

class PublicacionForm(forms.Form):
    Titulo = forms.CharField(max_length=30)
    Categoria = forms.CharField(max_length=80)
    Descripccion_Posteo = forms.CharField(max_length=500)
 
class BuscarPublicacionesForm(forms.Form):
    criterio_nombre = forms.CharField(max_length=50)