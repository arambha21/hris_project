from django import forms
from .models import TrainingSession

class TrainingSessionForm(forms.ModelForm):
    class Meta:
        model = TrainingSession
        fields = ['title', 'description', 'start_date', 'end_date', 'location', 'trainer', 'max_participants', 'participants']
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'participants': forms.CheckboxSelectMultiple(),
        }