"""restfulApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from .views import  *

urlpatterns = [

      path('genview/', EmployeeGeneric.as_view()),
      path('excel', ImportingAndExportingExcel.as_view()),
      path('genview/<id>/', EmployeeGenericPatchAndDelete.as_view()),
    # path('empdata/' , EmployeeAPI.as_view() ),
    # path('register/',UserTokenGenerator.as_view() )


    # path('emp', views.getEmpData, name='emp' ),
    # path('putemp/<id>', views.putemp, name='putemp' ),
    # path('deleteemp/<id>', views.deleteemp , name= 'delete')

]
