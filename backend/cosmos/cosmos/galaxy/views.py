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
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt



# ========================================================================chathistory===============================================

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import UserChatHistory
from .serializers import UserChatHistorySerializer

@api_view(['GET'])
def get_all_chats(request):
    chats = UserChatHistory.objects.all()
    serializer = UserChatHistorySerializer(chats, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_chat(request):
    serializer = UserChatHistorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_chat(request, pk):
    try:
        chat = UserChatHistory.objects.get(pk=pk)
        serializer = UserChatHistorySerializer(chat)
        return Response(serializer.data)
    except UserChatHistory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_chat(request, pk):
    try:
        chat = UserChatHistory.objects.get(pk=pk)
        serializer = UserChatHistorySerializer(chat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except UserChatHistory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_chat(request, pk):
    try:
        chat = UserChatHistory.objects.get(pk=pk)
        chat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except UserChatHistory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



# =======================================================CHATBOT ========================================================================>


from django.http import JsonResponse
from .pdf_processing import process_uploaded_pdfs, handle_user_question


@csrf_exempt
def upload_pdfs(request):
    if request.method == "POST":
        uploaded_pdfs = request.FILES.getlist('pdfs')
       
        x=process_uploaded_pdfs(uploaded_pdfs)
        print(x)
        return JsonResponse({"status": "success", "message": "PDFs processed successfully.","data":x["scripttext"],"pdfname":x["pdfname"],"pdfsize":x["pdfsize"]})
    return JsonResponse({"status": "error", "message": "Only POST requests are accepted."})

@csrf_exempt
def ask_question(request):
    if request.method == "POST":
        user_question = request.POST.get('question')
        
        # Validate that the user_question is a non-empty string
        if not user_question or not isinstance(user_question, str):
            return JsonResponse({"status": "error", "message": "Invalid question format."})

        response_data = handle_user_question(user_question)
        return JsonResponse(response_data)
    return JsonResponse({"status": "error", "message": "Only POST requests are accepted."})







# ===============================================================================================================================================
@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def login_user(request):
#     username = request.data.get("username")
#     password = request.data.get("password")

#     try:
#         user = User.objects.get(username=username)
#     except User.DoesNotExist:
#         return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

#     # Check if the provided password matches the one stored in the database
#     if check_password(password, user.password):
#         jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
#         jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
#         payload = jwt_payload_handler(user)
#         token = jwt_encode_handler(payload)
#         return Response({"token": token})
#     else:
#         return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)



        
@api_view(["POST"])
def login_user(request):
    try:
        # Fetching the email from request data
        email = request.data["email"]

        # Checking if the email exists in the database
        user_profile = UserProfile.objects.get(user__email=email)
        user_id = user_profile.user.id
        if user_profile:
            # Return a success response if the email exists
            
            return JsonResponse({"message": "Email found in database!","token":101, "user_id": user_id}, status=200)
        else:
            # Return a failure response if the email does not exist
            return JsonResponse({"message": "Email not found!"}, status=404)
    except UserProfile.DoesNotExist:
        # Return a failure response if the email does not exist
        return JsonResponse({"message": "Email not found!"}, status=404)
    except Exception as e:
        # Return a failure response if any exception occurs
        return JsonResponse({"message": f"An error occurred: {str(e)}"}, status=500)
    
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