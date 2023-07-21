from django import forms
from . models import Feedback

class feedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'feedback' : forms.TextInput(attrs={'class': 'form-control'})
        }