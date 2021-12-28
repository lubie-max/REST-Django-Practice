from django.contrib.auth.models import User
from rest_framework import fields, serializers

from .models import *

class UserSerializer(serializers.ModelSerializer):
   class Meta:
      model= User
      fields= ['username','password']


class EmployeeSerializers(serializers.ModelSerializer):

     class Meta:
        
        model= Employee
        # exclude = ['name']
        # feilds= ['name', 'salary']
        fields = '__all__'


     def validate(self, data):

         if  data['name']:
           for i in data['name']:
              if i.isdigit():
                 raise serializers.ValidationError({'Error':'Name should not containt numaric value.'})

         if data['salary']== 0  :
            raise serializers.ValidationError({"error":"Salary should not be 0"})

         return data
























# class CategorySerializer(serializers.ModelSerializer):

#    class  Meta:
#       model= Category
#       fields = ['category_name']


# class BookSerializer(serializers.ModelSerializer):
#    class Meta:
#       model= Book
#       fields= '__all__'


# class StudentSerializer(serializers.ModelSerializer):
#    category= CategorySerializer()
#    class Meta:
#       model= Student
#       fields = '__all__'

   
      