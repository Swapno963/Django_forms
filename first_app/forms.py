from django import forms
from django.core import validators

class contactForm(forms.Form):
    # required true mane aita ditai hobe, disable false mane user edit korta parbe nah
    name = forms.CharField(label='Full Name : ',initial='Sm',help_text='Total length must be within 70 char',required=False,disabled=False)

    # big text area
    name2 = forms.CharField(label='Full Name : ',help_text='Total length must be within 70 char',required=False, widget= forms.Textarea(attrs = {'id':'text_area','class':'class1 class2', 'placeholder':'Enter your name'}))

    # file =forms.FileField()
    # email = forms.EmailField(label='User Eamil')
    age = forms.CharField(widget=forms.NumberInput)
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    birthday = forms.CharField(widget=forms.DateInput(attrs= {'type':'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs= {'type':'datetime-local'}))
    # appointment2 = forms.DateTimeField()

    CHOICES = [('S','Small'),('M','Medium'),('L','Large')]
    size = forms.ChoiceField(choices = CHOICES, widget= forms.RadioSelect)

    MEAL = [('P','Pepperoni'),('M','Mashroom'),('C','Chicken')]
    pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)




class studentForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    # form validation
    def clean(self):
        cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        valemail = self.cleaned_data['email']

        if len(valname) < 10:
            raise forms.ValidationError("Enter a name at least 10 char")
        
        if '.com' not in valemail:
            raise forms.ValidationError('Your email must contain .com')
        




def len_check(value): # custom validator
    if len(value) < 10:
        raise forms.ValidationError('Enter a value at least 10 character')



# time to use built in validator
class DefaultData(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(10, message='Enter a name with min length of 10')])

    text = forms.CharField(widget=forms.TextInput, validators=[len_check])

    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message='Enter a valid email')])

    age = forms.IntegerField(validators=[validators.MaxValueValidator(18, message='Age greter then 30 is not allowed'),validators.MinValueValidator(30, message='Age less then 18 is not allowed')])

    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'], message='Only pdf are allowed')])






