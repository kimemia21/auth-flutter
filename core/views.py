from django.shortcuts import render
from django.shortcuts import get_object_or_404
from  .serializer import userSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["POST"])
def login(request):
    if request.method =="POST":
        data =request.data
        serialzer =userSerializer(data=data)
        if serialzer.is_valid():
            user =get_object_or_404(User,username =data["username"])
            if not user.check_password(password=data["password"]):
                return Response({"message":"user not found"},status=status.HTTP_400_BAD_REQUEST)
            return Response({"user":serialzer.data},status=status.HTTP_200_OK)
        

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
