from django import forms
from .models import reviews

class reviewsForm(forms.ModelForm):
    class Meta:
        model = reviews
        
        fields = ['review_movie', 'review_title', 'review_content']
        widgets = {
            'review_title' : forms.TextInput(attrs={'placeholder' : '제목 입력창'})
        }
        
        error_messages = {
            
        }
