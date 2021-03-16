
from django.urls import path
from .views import home_view, signup_view, awtomenzil_view, login_view, logout_view, settings_view, profile_view, statuschange_view

urlpatterns = [
    path('', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('awtomenzil/', awtomenzil_view, name='awtomenzil'),
    path('settings/', settings_view, name='settings'),
    path('profile/', profile_view, name='profile'),
    path('get/ajax/statuschange/', statuschange_view, name='statuschange'),
]
