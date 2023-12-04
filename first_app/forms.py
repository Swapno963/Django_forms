from django import forms

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