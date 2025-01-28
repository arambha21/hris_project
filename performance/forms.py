from django import forms
from .models import PerformanceReview

class PerformanceReviewForm(forms.ModelForm):
    class Meta:
        model = PerformanceReview
        fields = ['employee', 'reviewer', 'review_date', 'rating', 'comments', 'goals']
        widgets = {
            'review_date': forms.DateInput(attrs={'type': 'date'}),
            'comments': forms.Textarea(attrs={'rows': 4}),
            'goals': forms.Textarea(attrs={'rows': 4}),
        }