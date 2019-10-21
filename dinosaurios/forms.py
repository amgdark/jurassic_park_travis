from .models import Periodo, Dinosaurio
from django.forms import ModelForm,Textarea, TextInput


class PeriodoForm(ModelForm):

    class Meta:
        model = Periodo
        fields = '__all__'

        widgets = {
            'descripcion': Textarea(attrs={'cols': 6, 'rows': 2,'class':'form-control'}),
            'nombre':TextInput(attrs={'class':'form-control'}),
        }

class DinoForm(ModelForm):

    class Meta:
        model = Dinosaurio
        fields = '__all__'