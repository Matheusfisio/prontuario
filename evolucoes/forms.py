from django import forms
from .models import Evolucao

class EvolucaoForm(forms.ModelForm):
    class Meta:
        model = Evolucao
        fields = ['texto']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'texto': forms.Textarea(attrs={'rows': 5}),
        }