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


from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
import openai
import requests
from wikipedia import summary as wiki_summary
import json
from django.conf import settings
# =================================================================image generator ===================================================

@csrf_exempt
def generate_image(request):
    data = json.loads(request.body.decode('utf-8'))
    prompt = data.get('prompt',"")
    print(prompt)
    if not prompt:
        return JsonResponse({'error': 'Prompt not provided'}, status=400)

    # Define the endpoint and headers for the OpenAI API request
    endpoint = "https://api.openai.com/v1/images/generations"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {settings.OPENAI_API_KEY}",
    }
    data = {
        "prompt": prompt,
        "n": 1,
        "size": "1024x1024"
    }

    response = requests.post(endpoint, headers=headers, json=data)
    
    if response.status_code == 200:
        # You can extract required data from the response here
        image_data = response.json()
        return JsonResponse({'message': 'Image generation successful', 'data': image_data})
    else:
        return JsonResponse({'error': 'Failed to generate image'}, status=response.status_code)

# =========================================================================Text Analyzer===================================
def fetch_from_wikipedia(topic):
    try:
        return wiki_summary(topic, sentences=3)
    except:
        return "Sorry, I couldn't find up-to-date information on that topic."

@csrf_exempt
def ask(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        question = data.get('question', '')
        current_context = data.get('context', '')
        tone=data.get('tone', '')
        language=data.get('language','')
        # Initial response from GPT-3.5
        prompt = f"{current_context}\n\nQuestion: {question}\nAnswer:"
        response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": f"You are an assistant that answers questions based on provided context in {tone} tone and in write in {language} language."},
        {"role": "user", "content": f"Context: {current_context}"},
        {"role": "user", "content": f"Question: {question}"}
    ]
)


     



        gpt_answer = response['choices'][0]['message']['content']


        # Check if GPT's response indicates outdated data
        if "2021" in gpt_answer or "until 2021" in gpt_answer or "AI" in gpt_answer :
            # Extracting the main topic from the question for a focused Wikipedia search
            topic = question.split("about")[-1].strip() if "about" in question else question
            wiki_answer = fetch_from_wikipedia(topic)
            print(wiki_answer)
            return JsonResponse({"answer": wiki_answer})
        else:
            return JsonResponse({"answer": gpt_answer})

    else:
        return JsonResponse({"status": "error", "message": "Only POST method is allowed."})
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




        
@api_view(["POST"])
def login_user(request):
    try:
        # Fetching the email from request data
        email = request.data["email"]

        # Checking if the email exists in the database
        user_profile = UserProfile.objects.get(user__email=email)
        user_id = user_profile.id
        
        if user_profile:
            # Return a success response if the email exists
            
            return JsonResponse({"message": "Email found in database!","token":101, "user_id": user_id,}, status=200)
        else:
            # Return a failure response if the email does not exist
            return JsonResponse({"message": "Email not found!"}, status=404)
    except UserProfile.DoesNotExist:
        # Return a failure response if the email does not exist
        return JsonResponse({"message": "Email not found!"}, status=404)
    except Exception as e:
        # Return a failure response if any exception occurs
        return JsonResponse({"message": f"An error occurred: {str(e)}"}, status=500)
    

@api_view(['GET'])
def get_profile(request, user_id):
    try:
        user =user = User.objects.get(id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PATCH'])
def edit_user_profile(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
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


@api_view(['GET'])
def get_all_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)






