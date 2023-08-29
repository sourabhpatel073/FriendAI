from django.urls import path
from . import views

urlpatterns = [
    # User Profile URLs
    path('create_user/', views.create_user, name='create_user'),
    path('read_user/', views.read_user, name='read_user'),
    path('update_user/', views.update_user, name='update_user'),
    path('delete_user/', views.delete_user, name='delete_user'),

    # Chat URLs
    path('start_chat/', views.start_chat, name='start_chat'),
    path('view_chat/<int:chat_id>/', views.view_chat, name='view_chat'),
    path('delete_chat/<int:chat_id>/', views.delete_chat, name='delete_chat'),

    # Message URLs
    path('send_message/<int:chat_id>/', views.send_message, name='send_message'),
    path('view_message/<int:message_id>/', views.view_message, name='view_message'),
    path('delete_message/<int:message_id>/', views.delete_message, name='delete_message'),

    # PDF Document URLs
    path('upload_pdf/', views.upload_pdf, name='upload_pdf'),
    path('view_pdf/<int:pdf_id>/', views.view_pdf, name='view_pdf'),
    path('process_pdf/<int:pdf_id>/', views.process_pdf, name='process_pdf'),
    path('delete_pdf/<int:pdf_id>/', views.delete_pdf, name='delete_pdf'),

    # User History URLs
    path('view_history/', views.view_history, name='view_history')
]
