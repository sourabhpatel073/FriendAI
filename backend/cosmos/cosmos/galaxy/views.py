from django.contrib.auth.models import User
from rest_framework import status
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Chat, Message, PDFDocument, UserHistory, UserProfile
from .serializers import (UserSerializer, ChatSerializer, MessageSerializer, 
                          PDFDocumentSerializer, UserHistorySerializer)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if user:
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response({"token": token})
    else:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_profile(request):
    try:
        user = User.objects.get(username=request.user.username)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def edit_user_profile(request):
    try:
        user = User.objects.get(username=request.user.username)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_user_profile(request):
    try:
        user = User.objects.get(username=request.user.username)
        user.delete() # Deleting the user will automatically delete the associated UserProfile
        return Response(status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

# ... [rest of your views]






# from django.shortcuts import render

# # Create your views here.
# from django.contrib.auth.models import User
# from rest_framework import status
# from django.shortcuts import render, redirect
# from django.http import HttpResponse, JsonResponse
# from .models import User, Chat, Message, PDFDocument, UserHistory
# from .serializers import UserSerializer, ChatSerializer, MessageSerializer, PDFDocumentSerializer, UserHistorySerializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.contrib.auth import authenticate

# from rest_framework_jwt.settings import api_settings

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import UserProfile
# from .serializers import UserSerializer

# @api_view(['POST'])
# def register_user(request):
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
        
#         if serializer.is_valid():
#             user = serializer.save()
#             UserProfile.objects.get_or_create(user=user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def login_user(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     user = authenticate(username=username, password=password)
#     if user:
#         jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#         jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
#         payload = jwt_payload_handler(user)
#         token = jwt_encode_handler(payload)
#         return Response({"token": token})
#     else:
#         return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def user_profile(request):
#     try:
#         profile = UserProfile.objects.get(user=request.user)
#         serializer = UserSerializer(profile)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     except UserProfile.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

# @api_view(['PUT'])
# def edit_user_profile(request):
#     try:
#         profile = UserProfile.objects.get(user=request.user)
#         serializer = UserSerializer(instance=profile, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     except UserProfile.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

# @api_view(['DELETE'])
# def delete_user_profile(request):
#     try:
#         profile = UserProfile.objects.get(user=request.user)
#         profile.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     except UserProfile.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)