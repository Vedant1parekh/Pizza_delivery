"""pizza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pizzaapp import views
urlpatterns = [
    path('admin/',views.adminloginview,name="adminloginpage"),
    path('adminauthenticate/',views.authenntication),
    path('admin/homepage',views.adminhomepage,name="adminhomepage"),
    path('logout/',views.logoutadmin),
    path('addpizza/',views.addpizza),
    path('deletepizza/<int:y>/',views.deletepizza),
    path('',views.homepaegview,name="homepage"),
    path('signupuser/',views.signup),
    path('userauthenticate/',views.userauthenticate),
    path('loginuser/',views.userloginview,name="userloginpage"),
    path('customerpage/',views.customerwelcomeview,name="customerpage"),
    path('userlogout/',views.userlogout),
    path('placeorder/',views.placeorder),
    path('userorders/',views.myorders),
    path('adminorder/',views.adminorders,name="adminorder"),
    path('acceptorder/<int:userid>/',views.acceptorder),
    path('declineorder/<int:usrid>/',views.declineorder)
]
 