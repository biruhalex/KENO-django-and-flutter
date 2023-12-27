from django.forms import ModelForm
from .models import RanGenModel


class RanGenForm(ModelForm):
    class Meta:
        model = RanGenModel
        fields = '__all__'
