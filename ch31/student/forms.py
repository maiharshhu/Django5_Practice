from django import forms


class Registration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    # def clean_name(self):
    #     # name_value=self.cleaned_data.get('name')
    #     name_value = self.cleaned_data['name']
    #     if len(name_value)<4:
    #         raise forms.ValidationError('Enter more than or equal 4 char')
    #     return name_value
    
    # def clean_email(self):
    #     # name_value=self.cleaned_data.get('email')
    #     email_value = self.cleaned_data['email']
    #     if len(email_value)<20:
    #         raise forms.ValidationError('Enter more than or equal 20 char')
    #     return email_value
    
    def clean(self):
        cleaned_data = super().clean()
        name_value = cleaned_data.get('name')
        email_value = cleaned_data.get('email')
        
        if name_value and len(name_value) < 4:
            self.add_error('name','Enter more than and equal to 4 characters')
            
        if email_value and len(email_value) < 20:
            self.add_error('email', 'Enter more than or equal to 20 characters')
            
        return cleaned_data