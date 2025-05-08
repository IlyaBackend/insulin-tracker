'''Удобно описываем структуру и пишем меньше HTML кода, продолжаем лениться)))'''

from django import forms
from .models import InsulinInjection




class InjectionForm(forms.ModelForm):
    class Meta:
        model = InsulinInjection
        fields = ['injected', 'notes']