import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt # import

from .models import TaxiProfile, City, Category, Status #, TaxiStatus, TaxiCategory
from .forms import TaxiProfileModelForm ,UserModelForm #TaxiCategoryModelForm, TaxiStatusModelForm, 

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
                new_taxi = TaxiProfile(user_id=User.objects.get(username=form.cleaned_data['username']))
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
    return redirect('login')

# @csrf_exempt
def settings_view(request, *args, **kwargs):
    print('settings started working')
    if request.user.is_authenticated:
        print('user is authenticated')
        if request.method=='POST':
            # print('method is POST')
     
            # copyPOST = request.POST.copy()
            # print('nireden kontrol',copyPOST.get('nireden') if not copyPOST.get('nireden')=='' else 0)
            # print('nira kontrol',copyPOST.get('nira') if not copyPOST.get('nira')=='' else 0)
            # try:
            #     nireden = City.objects.filter(pk=copyPOST.get('nireden') if not copyPOST.get('nireden')=='' else 0).first()
            #     nira = City.objects.filter(pk=copyPOST.get('nira') if not copyPOST.get('nira')=='' else 0).first()
            #     category = Category.objects.filter(pk=copyPOST.get('category') if not copyPOST.get('category')=='' else 0).first()
            #     status = Status.objects.filter(pk=copyPOST.get('status') if not copyPOST.get('status')=='' else 0).first()
            #     # copyPOST['nireden'] = nireden
            #     # copyPOST['nira'] = nira
            #     copyPOST.pop('nireden')
            #     copyPOST.pop('nira')
            #     copyPOST.pop('category')
            #     copyPOST.pop('status')
            #     print('found nireden nira:', type(nireden), type(nira))
            # except:
            #     print('no status or category or nireden or nira was selected')
            form_profile=TaxiProfileModelForm(request.POST, request.FILES, instance = request.user.taxiprofile)
            form_user=UserModelForm(request.POST, instance=request.user)

            print('before checkin is_valid')
            if form_profile.is_valid()  and form_user.is_valid(): # and form_category.is_valid()
                print('they are valid')
                # form_user.instance.rel_user = request.user
                # form_profile.instance.rel_user = request.user
                form_profile.save()
                form_user.save()
                context={'form_profile': form_profile , 
                    'form_user': form_user}
                print('after save')
                
                # user=request.user
              
                # print('before profile')
                # # Here check TaxiProfile model, if exists update, if not create new taxe profile
                # try:
                #     check_profile=TaxiProfile.objects.get(user_id=user.id)
                #     # check_profile.user_id=user
                #     print(datetime.datetime.now())
                #     print('user photo none or not: ', form_profile.cleaned_data['user_photo'])
                #     print('car photo none or not: ', form_profile.cleaned_data['car_photo'])

                #     if form_profile.cleaned_data['user_photo']!='user_photo/default_taksist.png':
                #         print('inside form_profile comparing with default user photo')
                #         check_profile.user_photo=form_profile.cleaned_data['user_photo']
                #     if form_profile.cleaned_data['car_photo']!='car_photo/default_car.png':
                #         print('inside form_profile comparing with default car photo')
                #         check_profile.car_photo=form_profile.cleaned_data['car_photo']
                #     check_profile.mobile=form_profile.cleaned_data['mobile']
                #     print('before finding nireden nira')
                #     print('these will be assigned: ',nireden, nira)
                #     check_profile.nireden = nireden
                #     check_profile.nira = nira
                #     print('assigned nireden nira, and moving on to assign category and status')
                #     print('these will be assigned: ',category, status)
                #     check_profile.category = category
                #     print('category was assigned, and moving on to status')
                #     check_profile.status = status
                #     print('assigned nireden nira to check profile')
                #     print('user_photo to be assigned',request.FILES['user_photo'])
                #     print('user_photo to be assigned',request.POST.get('user_photo'))
                #     print('user_photo to be assigned',copyPOST.get('user_photo'))
                #     if request.FILES.get('user_photo') is None:
                #         print('user photo is none')
                #     else:
                #         check_profile.user_photo = request.FILES.get('user_photo')

                #     check_profile.save()
                #     print('saved taxiprofile')
                # except:
                #     print('exception happened when updating taxiprofile model')
                #     profile=form_profile.save(False)
                #     profile.user_id=user
                #     profile.save()
                #     print('saved profile with exception')
      
                # # Here update the User model data
                # try:
                #     current_user=User.objects.get(pk=request.user.id)
                #     print('user first name before: ', current_user.first_name)
                    
                #     current_user.first_name=form_user.cleaned_data['first_name']
                #     current_user.last_name=form_user.cleaned_data['last_name']
                #     current_user.save()
                #     print('user first name after: ', current_user.first_name)
                #     print(form_user.cleaned_data['first_name'])
                #     print('current user: ', current_user)
                # except:
                #     print('Exception occured when editing user model.')

                # msg='Successfully saved.'
                # context={'msg':msg}
                # print('return render')
                # # return render(request, 'profile.html', context)
                # return redirect('profile')
            else:
                print('form is not valied')
                msg='Forms are not valid'
                context={'msg':msg}
        else:
            print('settings method is get')
            try:
                # If user is authenticated then he exists in User table
                # This will not raise exception
                current_user=User.objects.get(pk=request.user.id)
                form_user=UserModelForm(instance=current_user)

                current_profile=TaxiProfile.objects.get(pk=request.user.id)
                form_profile=TaxiProfileModelForm(instance=current_profile)
                
                
            except:
                form_user=UserModelForm()
                form_profile=TaxiProfileModelForm()

            # cities_from = City.objects.all().exclude(pk=1).exclude(pk=2)
            # cities_to = City.objects.all().exclude(pk=1).exclude(pk=2)
            context={'form_profile': form_profile , 
                    'form_user': form_user}
                    # 'cities_from':cities_from,
                    # 'cities_to':cities_to }
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