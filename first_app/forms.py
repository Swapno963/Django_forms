from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label='User Name')
    email = forms.EmailField(label='User Eamil')
    age = forms.IntegerField()
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    birthday = forms.DateField()
    # appointment = forms.DateRangeField()
    appointment2 = forms.DateTimeField()