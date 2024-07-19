
from django.shortcuts import get_object_or_404
from  .serializer import userSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["POST"])
def login(request):
    if request.method =="POST":
        print("block1")
        data =request.data
        serialzer =userSerializer(data=data)
        if serialzer.is_valid():
            print("block2")
            user =get_object_or_404(User,username =data["username"])
            if not user.check_password(password=data["password"]):
                print("block3")
                return Response({"message":"user not found"},status=status.HTTP_400_BAD_REQUEST)
            print("block success")
            return Response({"user":serialzer.data},status=status.HTTP_200_OK)
        else:
            return Response(serialzer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    else:
        return Response({"error":"bad request method"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["POST"])
def signup(request):
    if request.method =="POST":
        data =request.data
        serialzer =userSerializer(data=data)
        if serialzer.is_valid():
            serialzer.save()
            user  =User.objects.get(username=data["username"])
            
            user.set_password(data["password"])
            user.save()
            return Response({"message":"User saved Corrected"},status=status.HTTP_200_OK)
        else:
            return Response(serialzer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
            
        
        
    else:
        return Response({"error":"bad request method"}, status=status.HTTP_400_BAD_REQUEST)        

@api_view(["GET"])
def all(request):
    if request.method =="GET":
        querySet =User.objects.all()
        serializer =userSerializer(querySet,many=True)
        if serializer.is_valid():
            
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        
    else:
        
        return Response({"error":"invalid request method"},status=status.HTTP_405_METHOD_NOT_ALLOWED)    
        
        
