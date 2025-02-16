from django import forms
from student.models import Profile

GENDER_CHOICE=(
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other'),
)

JOB_CITY_CHOICE = [
    ('Delhi', 'Delhi'),
    ('Pune', 'Pune'),
    ('Mumbai', 'Mumbai'),
    ('Bangalore', 'Bangalore'),
    ('Hyderabad', 'Hyderabad'),
    ('Chennai', 'Chennai'),
    ('Kolkata', 'Kolkata'),
    ('Ahmedabad', 'Ahmedabad'),
    ('Jaipur', 'Jaipur'),
    ('Lucknow', 'Lucknow'),
    ('Chandigarh', 'Chandigarh'),
    ('Indore', 'Indore'),
    ('Bhopal', 'Bhopal'),
    ('Kochi', 'Kochi'),
    ('Nagpur', 'Nagpur'),
    ('Surat', 'Surat'),
]


class ProfileForm(forms.ModelForm):
    gender =forms.ChoiceField(choices=GENDER_CHOICE,widget=forms.RadioSelect,help_text='(Choose any one)')
    
    job_city = forms.MultipleChoiceField(choices=JOB_CITY_CHOICE,widget=forms.CheckboxSelectMultiple,label="Preferred Job City",help_text='You can choose one then one options')
    
    class Meta:
        model=Profile
        fields=[ 'name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'email', 'job_city', 'profile_image', 'my_file' ]
        labels = {
            'name':'Full Name',
            'pin':'Pincode',
            'mobile':'Mobile Number',
            'dob':'Date Of Birth'
        }
        help_texts ={
            'profile_image':'Optional: Upload a profile image',
            'my_file':'Optional: Attach any additonal document(PDF,DOCX,etc)',
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'Datepicker','type':'Date'}),
            'locality':forms.TextInput(attrs={'class':'form-control','placeholder':'Write your area name.....'}),
            'city':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter City Name....'}),
            'pin':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter 6-Digits Pincode'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'mobile':forms.TextInput(attrs={'class':'form-control','placeholder':'10-Digit mobile number'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Address'}),
            
            
        }