from django import forms
from .models import MastersModel, SecPI1_Model

class MasterForm(forms.ModelForm):
    class Meta:
        model = MastersModel
        fields = "__all__"



class SecPI1Form(forms.ModelForm):
    class Meta:
        model = SecPI1_Model
        fields = "__all__"

