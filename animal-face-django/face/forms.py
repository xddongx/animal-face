from django import forms
from django.forms import ModelForm
from .models import FaceHist

# iterable 

  
# creating a form  
class FaceForm(forms.ModelForm): 
    class Meta:
        model = FaceHist
        fields = ['age', 'gender', 'image']
        labels = {
            'age': ('나이'),
            'gender': ('연령'),
            'image': ('이미지'),
        }
    # gender_field = forms.ChoiceField(choices = GENDER_CHOICES) 
    # age_field = forms.ChoiceField(choices=AGE_CHOICES)
