from django.urls import path
from . import views

app_name='account'

urlpatterns = [
    path('',views.index, name='home'),
    path('signin/',views.signin, name='signin'),
    path('signup/',views.signup, name='signup'),
    path('success/',views.reg_success, name='success'),
    path('signout/',views.signout, name="signout"),
]