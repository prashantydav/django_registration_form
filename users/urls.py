from django.urls import path
from .views import signup_view , signin_view , logout_view , home_view

app_name = "users"

urlpatterns = [
   
    path('signup/', signup_view , name = 'signup'),
    path('signin/', signin_view , name = 'signin'),
    path('logout/', logout_view , name = 'logout'),
    path('' , home_view , name = 'home')

]