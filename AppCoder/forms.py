from django import forms



class Curso_form(forms.Form):
    nombre = forms.CharField(max_lenght=40)
    comision = forms.IntergerField()