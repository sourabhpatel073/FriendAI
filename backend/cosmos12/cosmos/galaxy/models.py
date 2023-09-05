from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.URLField(max_length=500, null=True, blank=True)
    join_date = models.DateTimeField(auto_now_add=True)



class UserChatHistory(models.Model):
    user_id = models.CharField(max_length=255)
    messages = models.JSONField()
    date_of_post = models.DateTimeField(auto_now_add=True)
    # data = models.TextField()  # For storing the mentioned data point
    pdfsize = models.PositiveIntegerField()  # For storing the size of the PDF
    pdfname = models.CharField(max_length=255)  # For storing the name of the PDF



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
