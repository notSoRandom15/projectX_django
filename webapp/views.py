from django.shortcuts import render, redirect
from .forms import LoginForm, CreateUserForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required
from .models import Record

from django.contrib import messages


def home(request):
    return render(request, 'webapp/index.html')

    

# Register

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Account created successfully")

            return redirect('my-login')
        
    context = {'form': form}

    return render(request, 'webapp/register.html', context=context)


# Log in a user
def my_login(request):
    
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:

                auth.login(request, user)

                messages.success(request, "You have logged in")

                return redirect('dashboard')
    
    context = {'form':form}
    
    return render(request, 'webapp/my-login.html', context)


# - Dashboard

@login_required(login_url='my-login')
def dashboard(request):

    my_records = Record.objects.all()

    context = {'records': my_records}
    
    return render(request, 'webapp/dashboard.html', context)



# user logout

def user_logout(request):

    auth.logout(request)

    messages.success(request, 'User logged out')

    return redirect('my-login')


# create a record 

@login_required(login_url='my-login')
def create_record(request):
    
    form = CreateRecordForm()

    if request.method == 'POST':
        form = CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Record was created')

            return redirect('dashboard')
        
    context = {'form': form}    
    return render(request, 'webapp/create-record.html', context)


# update a record 

@login_required(login_url='my-login')
def update_record(request, pk):
    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)  # instance will be the id which is primary key

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)


        if form.is_valid():
            form.save()

            messages.success(request, 'Record was created')

            
            return redirect('dashboard')
        
    context = {'form': form}
    return render(request, 'webapp/update-record.html', context)

    
# read or view a singular record
@login_required(login_url='my-login')
def singular_record(request, pk):
    
    all_records = Record.objects.get(id=pk)

    context = {'record': all_records}

    return render(request, 'webapp/view-record.html', context)



# delete a record 

@login_required(login_url='my-login')
def delete_record(request, pk):
    record = Record.objects.get(pk=pk)

    record.delete()

    messages.success(request, 'Your record was deleted')


    return redirect('dashboard')


