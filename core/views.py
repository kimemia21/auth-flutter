
from django.shortcuts import get_object_or_404
from  .serializer import userSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
import json

@api_view(["GET"])
def all(request):
    if request.method =="GET":
        querySet = User.objects.all()
        serializer =userSerializer(querySet,many=True)
        print(type(serializer.data))
        return Response(serializer.data, status=status.HTTP_200_OK)
       
    
      
    else:
        return Response({"error":"not allowed"},status=status.HTTP_200_OK)
    
    
@api_view(["GET"]) 
def allOne(request,pk):
    if request.method =="GET":
        try:
            queryset =User.objects.get(id=pk)
            serializer =userSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
            
         
            
        
        except User.DoesNotExist:
            return Response("does not exist",status=status.HTTP_204_NO_CONTENT)
        
        
        


           

            
       
       
    
      
    else:
        return Response({"error":"not allowed"},status=status.HTTP_200_OK)   

# @api_view(["GET"])
# def all(request):
#     if request.method =="GET":
#         querySet =User.objects.all()
#         serializer =userSerializer(querySet,many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#         # else:
#         #     return Response(serializer.errors,status=status.HTTP_200_OK)
            
#     else:
#         return Response({"error":"invalid request method"},status=status.HTTP_405_METHOD_NOT_ALLOWED)    
        

@api_view(["POST"])
def signup(request):
    if request.method =="POST":
        data= request.data          
        serializer =userSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            user =User.objects.get(username=data["username"])
            user.set_password(data["password"])
            user.save()
            return Response("created succesfully",status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("use post",status=status.HTTP_502_BAD_GATEWAY)   
    



@api_view(["POST"])
def login(request):
    if request.method =="POST":
        print("block1")
        data =request.data
        # serializer =userSerializer(data=data)
        username =data["username"]
        password =data["password"]
        # email =data["email"]
        
        user =authenticate(username=username,password=password)
        if user is not None:
            serialzer =userSerializer(user)
            print(type(json.dumps(serialzer.data)))
            return Response(serialzer.data,status=status.HTTP_200_OK)
        else:
            return Response("username or password are invalid" ,status=status.HTTP_400_BAD_REQUEST) 
        
        
        # if serializer.is_valid():
        #     print("block2")
        #     user =get_object_or_404(User,username =data["username"])
        #     if not user.check_password(password=data["password"]):
        #         print("block3")
        #         return Response({"message":"user not found"},status=status.HTTP_400_BAD_REQUEST)
        #     print("block success")
        #     return Response({"user":serializer.data},status=status.HTTP_200_OK)
        # else:
        #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    else:
        return Response({"error":"bad request method"}, status=status.HTTP_400_BAD_REQUEST)
 