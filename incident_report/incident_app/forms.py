from django import forms 
from .models import Incident
class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ('category', 'description', 'images')  # Replace 'location' with 'address'
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
        }