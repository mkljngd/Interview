from django import forms
from .models import UserOfApp, Transaction
from datetime import date
from django.contrib.auth.forms import UserCreationForm
from back_end import calculate_age
from django.core.validators import RegexValidator

class UserForm(UserCreationForm):
     class Meta:
          model = UserOfApp
          fields = ['name', 'password1', 'password2', 'dob', 'mobile', 'pan', 'address', 'city', 'state'] 
          labels = {
               "dob" : "DOB (DD/MM/YYYY)"
          }
          exclude = ['interest', 'final_amount', 'loan_date']
     
     def clean_dob(self):
          dob = self.cleaned_data['dob']
          age = (date.today() - dob).days/365
          print(age)
          if age < 18:
               raise forms.ValidationError('Must be at least 18 years old to register')
          return dob
     # name = forms.CharField(label = "Name", max_length=100)
     # dob = forms.DateField(label = "DOB")
     # mobile = forms.
     # pan = forms.CharField(label = "PAN", max_length=100)

class TransactionForm(forms.Form):
     # user_mobile = forms.CharField(max_length = 10, validators=[RegexValidator(regex='^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$', message='Invalid Mobile Number', code='nomatch')])
     loan_amount = forms.IntegerField(max_value = 100000, min_value = 1)
     duration = forms.IntegerField(min_value = 1, label="Duration (Days)")
     rate = forms.ChoiceField(choices=((10,10), (15,15), (20,20)))


     class Meta:
          model = Transaction
          fields = '__all__' 
          labels = {
               "duration" : "Duration (Days)",
               "rate" : "Rate of Interest (p.a)"
          }

          # exclude = ['title', 'interest', 'final_amount', 'loan_date']
     # loan_amount = forms.IntegerField(max_value=100000, min_value = 1)
     # duration = forms.IntegerField(label = "Duration (Days)")
     # rate = forms.ChoiceField(label = "Rate of Interest (p.a)",choices=((10,10), (15,15), (20,20)))
     # today = date.today()
     # today = today.strftime("%d/%m/%Y")
     # transaction_date = forms.CharField(initial = today, disabled = True)
     
     
class LoginForm(forms.Form):
     mobile = forms.CharField(max_length = 10, validators=[RegexValidator(regex='^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$', message='Invalid Mobile Number', code='nomatch')])
     password = forms.CharField(widget=forms.PasswordInput())
