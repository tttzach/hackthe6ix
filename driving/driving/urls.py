"""driving URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from ht6p.views import FrontPageView, addLicense, addFname, addLname, TripView, SummaryView, addSpeed, ChangeCState, ChangeHState, stopState,startState
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ht6p/', FrontPageView),
    path('addLicense/',addLicense),
    path('addFname/',addFname),
    path('addLname/',addLname),


    path('trip/',TripView),
    path('summary/',SummaryView),
    path('startbutton/',startState),
    path('stopbutton/',stopState),
    path('newspeed/',addSpeed),
    path('ccstate/',ChangeCState),
    path('chstate/',ChangeHState),
]
