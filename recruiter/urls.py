from django.urls import path
from . import views
from django.contrib import admin
urlpatterns = [
    path('',views.home,name='home'),
    path('questions/<int:pk>',views.home1,name='questions'),
    path('login/',views.login,name='login'),#both are valid
    path('signup/',views.signup,name='signup'),
    path('logout/',views.signout),
    path('admin/',admin.site.urls),
]