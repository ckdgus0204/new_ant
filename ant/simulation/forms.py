
from django import forms
from ergate.models import Simulation
class Add_SimulationForm(forms.ModelForm):
    class Meta:
        model = Simulation
        fields = ['sname', 'uname','set_money', 'input','count']
