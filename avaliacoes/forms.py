# forms.py
from django import forms
from .models import Avaliacao

class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['area', 'articulacao', 'medidas_json']
        widgets = {
            'medidas_json': forms.Textarea(attrs={'rows': 4}),
        }
