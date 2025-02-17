from django import forms
from django.core.validators import MinLengthValidator, RegexValidator

# Field type example
GENDER_CHOICE = [('1','Male'),('2','Female'),('3','Other')]
INTEREST_CHOICES=[('1','Science'),('2','Art'),('3','Technology')]

# class DemoForm(forms.Form):
    # # basic field types
    # name = forms.CharField()
    # email = forms.EmailField()
    # pin_code = forms.IntegerField()

    # # additional fileds types
    # age = forms.FloatField()
    # date_of_birth = forms.DateField()
    # appointment_time = forms.TimeField()
    # appointment_datetime = forms.DateTimeField()
    # is_subscribed = forms.BooleanField()
    # agree_terms = forms.NullBooleanField()

    # # choice fields
    # gender = forms.ChoiceField(
    #     choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    # interests = forms.MultipleChoiceField(
    #     choices=[('tech', 'Technology'), ('art', 'Art'), ('sports', 'Sports')])

    # # File and URL fileds
    # profile_image = forms.ImageField()
    # resume = forms.FileField()
    # website = forms.URLField()

    # # Other Specailized Fields
    # phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$')
    # password = forms.CharField(widget=forms.PasswordInput())
    # slug = forms.SlugField()
    # ip_address = forms.GenericIPAddressField()
    # rating = forms.DecimalField()


class DemoForm(forms.Form):
    Name = forms.CharField(
        # label="CharField with TextInput",                 #Sets label Displayed next to the field
        max_length=100,                    #sets max length of characters to 100
        widget=forms.TextInput(attrs={'placeholder':'Type Here......', 'class':'mycss'}),
    )# Sets the suffix after the label (default is ":")
    
    
    Password = forms.CharField(
        #Password input (masks input for security)
        # label="Password Field",
        widget=forms.PasswordInput(
            attrs={'Placeholder':'Enter Password'})                  #Password Widget
    )
    
    hidden_field = forms.CharField(
        #Hidden input field (invisible to user)
        label="Hidden Field",
        #Hidden input widget for storing non-visible data
        widget=forms.HiddenInput()
    )
    
    Email = forms.CharField(
        # label="Email-Field",        #Email specific input field
        widget= forms.EmailInput(
            attrs={'placeholder':'name@example.com'})    #Email widget
    )
    
    Url = forms.URLField(
        label="URL Field",
        widget=forms.URLInput(
            attrs={'placeholder':'https://www.Example.com'}) #URL Widget
    )
    
    Pincode = forms.IntegerField(
        label="Number Field",                           #Number input field for integers
        # Number Input with min/max attributes
        widget=forms.NumberInput(attrs={'min':'0', 'max':'100'})
    )
    
    DOB = forms.DateField(
        label="Date Field",              #Date Input for dates only
        #Date widget with placeholder
        widget= forms.DateInput(attrs={'type':'Date','Placeholder':'YYYY-MM-DD'})
    )
    
    Meeting_time = forms.TimeField(
        label="Time Field",              #Time input field
        # Time widget with placeholder
        widget=forms.TimeInput(attrs={'type':'time','placeholder':'HH:MM:SS'})
    )
    
    datetime_field = forms.DateTimeField(
        #Date and Time filed for both date and time
        label="DateTime Field",            
        widget=forms.DateTimeInput(
            attrs={'type':'datetime-local','placeholder':'YYYY-MM-DD HH:MM:SS'})
    )
    
    #TEXT area 
    Post_content = forms.CharField(
        #Text area field for writing
        # label = "Textarea Field",
        widget=forms.Textarea(attrs={'Placeholder':'Enter Some Details About..........'})
    )
    
    # Checkbox widgets
    boolean_filed = forms.BooleanField(
        label='boolean field',
        widget=forms.CheckboxInput()
    )
    
    null_boolean_field = forms.NullBooleanField(
        label = "Null Boolean Field",
        widget=forms.NullBooleanSelect()
    )
    
    choice_field = forms.ChoiceField(
        label="choice Field",
        choices=GENDER_CHOICE,
        widget=forms.Select()
    )
    
    multiple_choice_field = forms.MultipleChoiceField(
        label="Multiple choice Field",
        choices=INTEREST_CHOICES,
        widget=forms.SelectMultiple()
    )
    
    Radio_choice_field = forms.ChoiceField(
        label="Radio choice Field",
        choices=GENDER_CHOICE,
        widget=forms.RadioSelect()
    )
    
    File_Field = forms.FileField(
        widget=forms.FileInput()
    ) 
    
    Image_Field = forms.ImageField(
        widget=forms.ClearableFileInput()
    )
    
    # Other Specilized Widget
    slug_field = forms.SlugField(
        #Slug (URL-Friendly) input field
        label = "Slug Field",
        widget=forms.TextInput(attrs={'placeholder':'my-slug'})
    )
    
    ip_address_field = forms.GenericIPAddressField(
        label="Ip Address Field",
        widget=forms.TextInput(attrs={'placeholder':'0.0.0.0'})
    )
    
    time_duration_field = forms.DurationField(
        label = "Duration Field",
        widget=forms.TextInput(attrs={'placeholder':'HH:MM:SS '})
    )
    
    decimal_field = forms.DecimalField(
        label="Decimal Field",
        max_digits=5,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'step':'0.1','placeholder':'0.0'})
    )
    
    split_date_time = forms.SplitDateTimeField(
        label = "Split date and time field",
        widget=forms.SplitDateTimeWidget()
    )
     
    split_hidden_date_time = forms.SplitDateTimeField(
        label = "Split Hidden date and time field",
        widget=forms.SplitHiddenDateTimeWidget()
    )