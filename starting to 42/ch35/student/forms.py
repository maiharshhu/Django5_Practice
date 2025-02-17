from django import forms
from student.models import Profile
    
# class Registration(forms.Form):
#     name = forms.CharField(error_messages={'required':'Name is Required'})
#     email = forms.EmailField(error_messages={'required':'Email is required'})
#     password = forms.CharField(
#         error_messages={'required':'Name is required'},widget=forms.PasswordInput )
    
class Registration(forms.ModelForm):
    name = forms.CharField(max_length=50, required=False)
    confirm_password = forms.CharField()
    
    class Meta:
        model = Profile
        # fields = ['name', 'email', 'password']
        # To see all the model fields at once means do not need to call one by one
        fields = '__all__'
        # exclude the filed that we don't want in form
        # exclude = ['password']
        labels = {'name':'Enter Name', 'email':'Enter Email'}
        error_messages ={
            'email':{'required':'Email is Required'}
        }
        widgets ={
            'password':forms.PasswordInput(attrs={'class':'pwdclass'}),
            'name':forms.TextInput(attrs={'class':'Myclass', 'placeholder':'Enter your name...'})
        }