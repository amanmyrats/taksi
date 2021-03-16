from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import JsonResponse

from .models import TaxiProfile , TaxiStatus, TaxiCategory
from .forms import TaxiProfileModelForm ,TaxiCategoryModelForm, TaxiStatusModelForm, UserModelForm

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
            form=UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username=form.cleaned_data.get('username')
                raw_password=form.cleaned_data.get('password1')
                user=authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('home')
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
    return redirect('login')

def settings_view(request, *args, **kwargs):
    print('settings started working')
    if request.user.is_authenticated:
        print('user is authenticated')
        if request.method=='POST':
            print('method is POST')
            form_profile=TaxiProfileModelForm(request.POST, request.FILES)
            form_category=TaxiCategoryModelForm(request.POST)
            # form_status=TaxiStatusModelForm(request.POST)
            form_user=UserModelForm(request.POST)
            print('before checkin is_valid')
            if form_profile.is_valid() and form_category.is_valid() and form_user.is_valid():
                user=request.user
              
                print('before profile')
                # Here check TaxiProfile model, if exists update, if not create new taxe profile
                try:
                    check_profile=TaxiProfile.objects.get(user_id=user.id)
                    # check_profile.user_id=user
                    print('photo none or not: ', form_profile.cleaned_data['user_photo'])
                    if form_profile.cleaned_data['user_photo']!='user_photo/default_taksist.png':
                        check_profile.user_photo=form_profile.cleaned_data['user_photo']
                    if form_profile.cleaned_data['car_photo']!='car_photo/default_car.png':
                        check_profile.car_photo=form_profile.cleaned_data['car_photo']
                    check_profile.mobile=form_profile.cleaned_data['mobile']
                    check_profile.save()
                    print('saved profile')
                except:
                    profile=form_profile.save(False)
                    profile.user_id=user
                    profile.save()
                    print('saved profile with exception')
      
                # Here check TaxiCategory model, if exists update, if not create new taxe category
                try:
                    check_category=TaxiCategory.objects.get(user_id=user.id)
                    # check_category.user_id=user
                    check_category.name=form_category.cleaned_data['name']
                    check_category.save()
                    print('saved category')
                except:
                    category=form_category.save(False)
                    category.user_id=user
                    category.save()
                    print('saved category with exception')
                # Here check TaxiStatus model, if exists update, if not create new taxe status
                # try:
                #     check_status=TaxiStatus.objects.get(user_id=user.id)
                #     # check_status.user_id=user
                #     check_status.status=form_status.cleaned_data['status']
                #     check_status.save()
                    
                # except:
                #     status=form_status.save(False)
                #     status.user_id=user
                #     status.save()

                # Here update the User model data
                try:
                    current_user=User.objects.get(pk=request.user.id)
                    print('user first name before: ', current_user.first_name)
                    
                    current_user.first_name=form_user.cleaned_data['first_name']
                    current_user.last_name=form_user.cleaned_data['last_name']
                    current_user.save()
                    print('user first name after: ', current_user.first_name)
                    print(form_user.cleaned_data['first_name'])
                    print('current user: ', current_user)
                except:
                    print('Exception occured when editing user model.')

                msg='Successfully saved.'
                context={'msg':msg}
                print('return render')
                # return render(request, 'profile.html', context)
                return redirect('profile')
            else:
                msg='Forms are not valid'
                context={'msg':msg}
        else:
            current_profile=TaxiProfile.objects.get(pk=request.user.id)
            current_user=User.objects.get(pk=request.user.id)
            current_category=TaxiCategory.objects.get(pk=request.user.id)

            form_profile=TaxiProfileModelForm(instance=current_profile)
            form_category=TaxiCategoryModelForm(instance=current_category)
            # form_status=TaxiStatusModelForm()
            form_user=UserModelForm(instance=current_user)

            context={'form_profile': form_profile, 'form_category': form_category , 'form_user': form_user  }
    else:
        return redirect('home')
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
    if request.is_ajax() and request.method=='GET':
        print("inside statuschange_view")
        new_status=request.GET.get('status', None)
        user_status=TaxiStatus.objects.get(pk=request.user.id)
        user_status.status=new_status
        user_status.save()
        return JsonResponse({"new_status":new_status}, status = 200)