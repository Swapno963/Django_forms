from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label='User Name')
    file =forms.FileField()
    # email = forms.EmailField(label='User Eamil')
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    # birthday = forms.DateField()
    # # appointment = forms.DateRangeField()
    # appointment2 = forms.DateTimeField()

    # CHOICES = [('S','Small'),('M','Medium'),('L','Large')]
    # size = forms.ChoiceField(choices = CHOICES)

    # MEAL = [('P','Pepperoni'),('M','Mashroom'),('C','Chicken')]
    # pizza = forms.MultipleChoiceField(choices=MEAL)