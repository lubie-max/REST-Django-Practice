from django.contrib.auth import authenticate
from django.db.models.query import QuerySet
from django.shortcuts import render,HttpResponse
from rest_framework import response
from rest_framework import authentication
from rest_framework import views
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import *
from .models import *
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
# Create your views here.


# [3].Generic views
# just to avoid huge code writing
from rest_framework import generics

class EmployeeGeneric(generics.ListAPIView, generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers


class EmployeeGenericPatchAndDelete(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    lookup_field= 'id'
    
   











# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# # [2] i. Token Generation. ii.jwt

# class UserTokenGenerator(APIView):
#     def post(self, request):
#         srl= UserSerializer(data=request.data)
#         if not srl.is_valid():
#             return Response({'error':srl.errors})

#         srl.save()

#         user= User.objects.get(username = srl.data['username'])
#         token_obj, _ = Token.objects.get_or_create(user=user)
#         print(user)

#         return Response({'token':str(token_obj), 'data':srl.data})




# #i. token authentication 
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated

# #ii. jwt authentication
# from rest_framework_simplejwt.authentication import JWTAuthentication


# class EmployeeAPI(APIView):
#     # <<<< Token Authentication>>>
#     # authentication_classes= [TokenAuthentication]
#     # permission_classes= [IsAuthenticated]

#     # <<<<< JWT Authentication >>>>>>
#     authentication_classes= [JWTAuthentication ]
#     permission_classes= [IsAuthenticated]
#     def get(self, request):

       
#            empObj= Employee.objects.all()
#            serl= EmployeeSerializers(empObj, many= True)
#            print(request.user)
#            user= request.user
#            return Response({'data':serl.data})
           

#     def post(self, request):
#         data =request.data
#         serl= EmployeeSerializers(data=request.data)
#         if not serl.is_valid():
#             return Response({'status':111, 'error': serl.errors})

#         serl.save()
#         return Response({'data':data})


#     def patch(self, request):
#         try:
#             empObj= Employee.objects.get(id= request.data['id'])
#             serl= EmployeeSerializers(empObj, data=request.data,  partial= True)
#             if not serl.is_valid():
#                 return Response({'status':serl.errors})

#             serl.save()
#             return Response({'status':serl.data, 'message':"Record Updated Successfully."})

#         except Exception as e:
#             print(e)
#             return Response({'msg':'Something Went Wrong.'})


#     def put(self,request):
#         try:
#              empObj= Employee.objects.get(id= request.data['id'])
#              serlizer= EmployeeSerializers(empObj, data=request.data)
#              if not serlizer.is_valid():
#                  return Response({'status':serlizer.errors})
             
#              serlizer.save()
#              return Response({"Status":"Record updated successfully."})

#         except Exception as e:
#             print(e)
#             return Response({'Status':'Something Went Wrong.'})



#     def delete(self,request):
#         id= request.GET.get('id')
#         empObj= Employee.objects.get(id= id)
#         empObj.delete()
#         return Response({'Status':'Record Deleted Successfully.'})











# ......................................................................................................
# [1] @api_view,  CRUD and Serializers
# @api_view(['GET'])
# def home(request):
#     # return HttpResponse('Hi there')
#     empObj= Employee.objects.all()
#     serl= EmployeeSerializers(empObj, many= True)


#     return Response({'status': 200 , 'data': serl.data})


# @api_view(['POST'])
# def getEmpData(request):
#     data =request.data
#     serlz= EmployeeSerializers(data= request.data)
#     #
#     print(data)
#     if not serlz.is_valid():   
#         return Response({'status': 200 , 'data': serlz.errors ,'Message':'You sent This'})
#     serlz.save()
#     return Response({'status': 200 , 'data': data ,'Message':'You sent This'})

    

# @api_view(['PUT'])
# def putemp(request, id):
#    try: 
        
#         empObj= Employee.objects.get(id= id)
#         serializer= EmployeeSerializers( empObj,data=request.data ,partial= True) #set partial = True for Patching

#         if not serializer.is_valid():   
#                  return Response({'status': 200 , 'data': serializer.errors ,'Message':'You sent This'})
#         serializer.save()
#         return Response({'status': 200 , 'data': serializer.data ,'Message':'You sent This'})

#    except Exception as e:
#         return Response({'error':'Something you missed.'})



# @api_view(['DELETE'])
# def deleteemp(request, id):
#     try:
#         empobj= Employee.objects.get(id= id)
#         empobj.delete()
#         return Response({'status': '123','Message':'Deleted Successfully'})

#     except Exception as e:
#         print(e)
#         return Response({'msg':'Somthing Went Wrong'})


# ..............................................................................................................

# @api_view(['GET'])
# def home(request):
#     studentObj= Student.objects.all()
#     serl= StudentSerializer(studentObj, many= True)

#     return Response({'data':serl.data})

