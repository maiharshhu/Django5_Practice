from django import forms
from school.models import Profile

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['student_name','email','password']
        
        
class TeacherRegistration(StudentRegistration):
    class Meta(StudentRegistration.Meta):
        fields = ['teacher_name','email','password']
        