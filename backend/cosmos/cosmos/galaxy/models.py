from django.db import models

# Create your models here.
from django.conf import settings

# User Model
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True) # Optional field
    join_date = models.DateTimeField(auto_now_add=True)

# Chat Model
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats')
    timestamp = models.DateTimeField(auto_now_add=True) # Represents the initiation of the chat


# Message Model
class Message(models.Model):
    SYSTEM = 'SYSTEM'
    USER = 'USER'
    SENDER_CHOICES = [
        (SYSTEM, 'System'),
        (USER, 'User')
    ]
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender_type = models.CharField(max_length=6, choices=SENDER_CHOICES, default=USER) # To distinguish between system and user messages
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    attachments = models.ForeignKey('PDFDocument', null=True, blank=True, on_delete=models.SET_NULL) # Optional field


# PDF Document Model
class PDFDocument(models.Model):
    title = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_documents')
    upload_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=True, blank=True) # This can store the extracted text content from the PDF if needed
    embedding = models.TextField() # Will store the generated semantic embedding of the document


class UserHistory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='history')
    messages = models.ManyToManyField(Message, blank=True) # Messages sent/received by the user
    uploaded_pdfs = models.ManyToManyField(PDFDocument, blank=True) # PDFs uploaded by the user
