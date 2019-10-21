from django.forms import ModelForm
from .models import Periodo, Dinosaurio


class PeriodoForm(ModelForm):

    class Meta:
        model = Periodo
        fields = '__all__'

class DinoForm(ModelForm):

    class Meta:
        model = Dinosaurio
        fields = '__all__'