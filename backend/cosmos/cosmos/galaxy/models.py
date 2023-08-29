from django.db import models

# Create your models here.
from django.conf import settings

# User Model
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    join_date = models.DateTimeField(auto_now_add=True)

# Chat Model
class Chat(models.Model):
    participants = models.ManyToManyField(User, related_name='chats')
    timestamp = models.DateTimeField(auto_now_add=True)

# Message Model
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(upload_to='pdf_attachments/', null=True, blank=True)

# PDF Document Model
class PDFDocument(models.Model):
    title = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_documents')
    upload_date = models.DateTimeField(auto_now_add=True)
    embedding = models.TextField()  # This will hold the semantic embedding, which you'll generate externally.

# User History Model
# This is a bit complex since it needs to track both messages and PDFs. 
# For simplicity, we'll represent them as text logs.
class UserHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='history')
    log = models.TextField()  # A textual representation of the action, like "Sent a message" or "Uploaded a PDF".
    timestamp = models.DateTimeField(auto_now_add=True)
