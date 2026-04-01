from django import forms
from .models import Inscricao


class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ['nome', 'email', 'telefone', 'nascimento', 'descricao']
        widgets = {
            'nome':       forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome completo'}),
            'email':      forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'seu@email.com'}),
            'telefone':   forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(00) 00000-0000'}),
            'nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'descricao':  forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Fale um pouco sobre você...'}),
        }
