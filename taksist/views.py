import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import JsonResponse

from .models import TaxiProfile, City, Category, Status
from .forms import TaxiProfileModelForm ,UserModelForm


def home_view(request):
    return render(request, 'home.html', {'msg':'Hello'})


def signup_view(request):
    if request.user.is_authenticated:
        print('You are already in.')
        print(request.user)
        context={}
        return render(request, 'home.html', context)
    else:
        if request.method=='POST':
            print('in post')
            form=UserCreationForm(request.POST)
            if form.is_valid():
                print('in VALID')
                form.save()

                # Create an instance in TaxiProfile Model as well
                new_taxi = TaxiProfile(user=User.objects.get(username=form.cleaned_data['username']))
                new_taxi.save()

                username=form.cleaned_data.get('username')
                raw_password=form.cleaned_data.get('password1')
                user=authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('home')
            else: # if not valid
                errors = form.errors
                form=UserCreationForm()
                return render(request, 'signup.html', {'form':form, 'errors':errors})
        else:
            form=UserCreationForm()
        return render(request, 'signup.html', {'form': form})


def login_view(request):
    context={}
    if request.user.is_authenticated:
        return redirect('home')
    else:
        print('user is not authenticated')
        if request.method=='POST':
            print('request method is POST')
            username=request.POST.get('username')
            raw_password=request.POST.get('password')
            user=authenticate(username=username, password=raw_password)
            print('this is result of user: ', user)
            if user is not None:
                # redirect ('profile.html')
                print('before login')
                login(request, user)
                print('user authenticated')
                print('this is result', user.is_authenticated)
                return render(request, 'profile.html', {'profile_data':request.user})

            else:
                msg='Agza adyňyz ýada parolyňyz ýalňyş, täzeden synanşyň.'
                context={'msg':msg}

            return render(request, 'profile.html', {'msg2':'hello asdg'})
        return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


def settings_view(request, *args, **kwargs):
    print('settings_view started working')
    if request.user.is_authenticated:
        print('user is authenticated')
        if request.method=='POST':
            form_profile=TaxiProfileModelForm(request.POST, request.FILES, instance = request.user.taxiprofile)
            form_user=UserModelForm(request.POST, instance=request.user)

            if form_profile.is_valid()  and form_user.is_valid(): # and form_category.is_valid()
                print('content of POST')
                for setir in request.POST:
                    
                    print(setir,request.POST[setir])
                print('content of FILES')
                for ozel in request.FILES:
                    
                    print(ozel,request.FILES[ozel])
                form_profile.save()
                form_user.save()
                return redirect('profile')
                
            else:
                msg='Forms are not valid'
                context={'msg':msg}
        else:
            print('settings method is get')
            try:
                # If user is authenticated then he exists in User table
                # This will not raise exception
                current_user=User.objects.get(pk=request.user.id)
                form_user=UserModelForm(instance=current_user)
            except:
                form_user=UserModelForm()

            try:
                # If user is authenticated then he exists in TaxiProfile table
                # This will not raise exception
                current_profile=TaxiProfile.objects.get(pk=request.user.id)
                form_profile=TaxiProfileModelForm(instance=current_profile)
            except:
                form_profile=TaxiProfileModelForm()

            context={'form_profile': form_profile , 
                    'form_user': form_user}

    else:
        return redirect('home')
    cities = City.objects.all()
    context['cities'] = cities
    return render(request, 'settings.html', context)


def profile_view(request):
    if request.user.is_authenticated:
        # profile_data=request.user
        context={'msg':'Successful'}
        return render(request, 'profile.html', context)
    else:
        # if request.method=='POST':
        #     return render(request, 'login.html', {})
        context={'msg':'Failed'}
        return render(request, 'profile.html', context)


def awtomenzil_view(request):
    return render(request, 'awtomenzil.html', {'msg': 'Hello'})


def statuschange_view(request):
    pass
    if request.is_ajax() and request.method=='GET':
        print("inside statuschange_view")
        new_status=request.GET.get('status', None)
        print('new status', new_status)
        status_object = Status.objects.get(name = new_status)

        user = TaxiProfile.objects.get(user_id = request.user)
        user.status = status_object
        user.save()

        return JsonResponse({"new_status":new_status}, status = 200)


def test_view(request):
    return render(request, 'test.html', {'msg':'test'})