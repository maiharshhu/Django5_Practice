from django import forms
from django.core import validators

# custom validateor
def starts_with_s(value):
    if value[0]!='s':
        raise forms.ValidationError('Email Should start with s')
    
# Built in Validators
class Registration(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(10),
                                       validators.MinLengthValidator(3)])
    email = forms.EmailField(validators=[starts_with_s])
    password = forms.CharField(widget=forms.PasswordInput)
    
