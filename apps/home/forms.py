# forms.py

from django import forms
from .models import Pessoa

class PessoaForm(forms.Form):
        mensagem = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 5}))