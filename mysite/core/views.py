from django.shortcuts import render, redirect
from .forms import UserForm, TransactionForm, LoginForm
from .models import UserOfApp
from datetime import date, timedelta
from back_end import compound_interest, calculate_age
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

LOAN_LIMIT = 100000


@login_required(login_url="login")
def home(request):
     print(UserOfApp.objects.all())
     users = [i for i in UserOfApp.objects.all()]
     data= {'users':users}
     return render(request, 'home.html',data)

# def authenticateuser(request):
#      device = request.POST['device'].split(" ")[0]
#      # device = 'web'
#      pass
#      return render(request, 'home.html')


def register(request):
     if request.method == 'POST':
          form = UserForm(request.POST)
          if form.is_valid():
               # form.save()
               name = form.cleaned_data['name']
               dob = form.cleaned_data['dob']
               mobile = form.cleaned_data['mobile']
               pan = form.cleaned_data['pan']
               address = form.cleaned_data['address']
               city = form.cleaned_data['city']
               state = form.cleaned_data['state']
               password = form.cleaned_data['password1']
               p = UserOfApp.objects.create_user(name = name, dob = dob, mobile = mobile, pan = pan, address = address,city = city, state = state, username = mobile, password = password, loan_limit = LOAN_LIMIT)
               p.save()
               print('saved')
               # print(f'age is {calculate_age(dob)}')
               # return redirect('home')
     else:
          form = UserForm()
     return render(request, 'register.html', {'form' : form})

     # form = UserForm()
     # return render(request, 'register.html', {"form" :  form})

# @login_required(login_url="login")
def transaction(request):
     if request.method == "POST":
          form = TransactionForm(request.POST)
          if form.is_valid():
               loan_amount = int(form.cleaned_data['loan_amount'])
               duration = int(form.cleaned_data['duration'])
               rate = int(form.cleaned_data['rate'])
               interest = compound_interest(loan_amount, rate, duration)
               print(interest)
               transaction_date =  date.today()
               due_date = transaction_date + timedelta(duration) 
               print(due_date)
               final_amount = loan_amount + interest
               print(final_amount)
               user = request.user
               user.interest = interest
               user.final_amount = final_amount
               user.due_date = due_date
               user.save()
               print('updated')
               print('LOLOLOLOLOLOL', user.name, user.password)
               # Transaction(uid=User.objects.filter(mobile=))
     else:
          form = TransactionForm()
          user = None
     today = date.today()
     today = today.strftime("%d/%m/%Y")
     return render(request, 'transaction.html', {'form' : form, 'today': today, 'user' : user})


def logoutuser(request):
     logout(request)
     return redirect('home')


def loginuser(request):
     print('lol1')
     if request.method == "POST":
          print('lol2')
          # form = LoginForm(request.POST)
          mobile = request.POST['mobile']
          password = request.POST['password']
          user = authenticate(username=mobile, password=password)
          print(mobile,password,"\n\n\n\n\n\n\n\n\n\n")
          # login(request, user)
          if user is not None:
               login(request, user)
               return redirect('home')
               # return render(request, 'home.html')
          else:
               return render(request, 'login.html', {'loginFail': True})
     else:
          form = LoginForm()
     return render(request, 'login.html', {'form': form})