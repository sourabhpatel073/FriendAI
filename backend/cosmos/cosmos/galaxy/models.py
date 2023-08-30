from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    join_date = models.DateTimeField(auto_now_add=True)

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chats')
    timestamp = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    SYSTEM = 'SYSTEM'
    USER = 'USER'
    SENDER_CHOICES = [
        (SYSTEM, 'System'),
        (USER, 'User')
    ]
    
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender_type = models.CharField(max_length=6, choices=SENDER_CHOICES, default=USER)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    attachments = models.ForeignKey('PDFDocument', null=True, blank=True, on_delete=models.SET_NULL)

class PDFDocument(models.Model):
    title = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_documents')
    upload_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=True, blank=True)
    embedding = models.TextField()

class UserHistory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='history')
    messages = models.ManyToManyField(Message, blank=True)
    uploaded_pdfs = models.ManyToManyField(PDFDocument, blank=True)
