
from django import forms
from ergate.models import Autoset
class Add_AutosetForm(forms.ModelForm):
    class Meta:
        model = Autoset
        fields = ['sname', 'uname','set_money', 'input','count']
