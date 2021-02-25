from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.
class UserOfApp(AbstractUser):
     # title = models.CharField( default = "",max_length = 100)
     name = models.CharField( max_length = 100)
     dob = models.DateField()
     mobile = models.CharField(unique = True, max_length = 10, validators=[RegexValidator(regex='^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$', message='Invalid Mobile Number', code='nomatch')])
     pan = models.CharField( max_length = 20)
     address = models.TextField(default = "", max_length = 200)
     city = models.CharField( default = "", max_length = 50)
     state = models.CharField( default = "", max_length = 50)
     interest = models.FloatField(default = None, null=True)
     final_amount = models.FloatField(default = None, null=True)
     loan_date = models.DateField(default = None, null=True)
     loan_limit = models.IntegerField(default=100000)

     def __str__(self): 
          return self.mobile


class Transaction(models.Model):
     uid = models.ForeignKey(UserOfApp, on_delete=models.CASCADE, db_column='uid')
     loan_amount = models.IntegerField(default=0.0)
     duration = models.IntegerField(default=0)
     rate = models.IntegerField(default=0)
          



# Create your models here.