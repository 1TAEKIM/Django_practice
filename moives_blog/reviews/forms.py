from django import forms
from .models import reviews, Comment

class reviewsForm(forms.ModelForm):
    class Meta:
        model = reviews
        
        fields = ['review_movie', 'review_title', 'review_content']
        widgets = {
            
            
            'review_title' : forms.TextInput(attrs={'placeholder' : '제목 입력창', 
                                                    'class':'review_title'}),
            
        }
        
        error_messages = {
            
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']