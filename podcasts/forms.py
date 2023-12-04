from django.forms import ModelForm, widgets
from django import forms
from .models import Review,ReviewEpisode

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']    
        labels = {
            'value': 'Your rating',
            'body': 'Add a comment with your rating'
        }

    def __init__(self,*args,**kwargs):
        super(ReviewForm,self).__init__(*args,**kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class ReviewForm2(ModelForm):
    class Meta:
        model = ReviewEpisode
        fields = ['value', 'body']    
        labels = {
            'value': 'Your rating',
            'body': 'Add a comment with your rating'
        }

    def __init__(self,*args,**kwargs):
        super(ReviewForm2,self).__init__(*args,**kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})