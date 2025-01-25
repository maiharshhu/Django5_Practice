from django import forms


class Registration(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField(initial="hii")
    email = forms.EmailField()
    city = forms.CharField()


class Address(forms.Form):
    name = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    pin_code = forms.IntegerField()
