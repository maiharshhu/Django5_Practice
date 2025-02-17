from django import forms

# class Registration(forms.Form):
#     name = forms.CharField(error_messages={'required':'Name is Required'})
#     email = forms.EmailField()
#     password = forms.CharField(
#         error_messages={'required':'Name is required'},widget=forms.PasswordInput,min_length=5, max_length=50)
    

class Registration(forms.Form):
    error_css_class = 'myerror'
    required_css_class = 'required'
    name = forms.CharField(error_messages={'required':'Name is Required'})
    email = forms.EmailField()
    password = forms.CharField(
        error_messages={'required':'Name is required'},widget=forms.PasswordInput,min_length=5, max_length=50)
    