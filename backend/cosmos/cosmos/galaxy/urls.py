from django.urls import path
from . import views

urlpatterns = [
    # User Profile URLs
    path('user_register/', views.register_user, name='register_user'),
    path('user_login/', views.login_user, name='login_user'),
    path('user/profile/', views.user_profile, name='user_profile'),
    path('user/edit/', views.edit_user_profile, name='edit_user_profile'),
    path('user/delete/', views.delete_user_profile, name='delete_user_profile'),

    # Chat URLs
    # path('chats/start/', views.start_chat, name='start_chat'),
    # path('chats/<int:chat_id>/', views.view_chat, name='view_chat'),
    # path('chats/<int:chat_id>/delete/', views.delete_chat, name='delete_chat'),

    # # Message URLs
    # path('chats/<int:chat_id>/send_message/', views.send_message, name='send_message'),
    # path('messages/<int:message_id>/', views.view_message, name='view_message'),
    # path('messages/<int:message_id>/delete/', views.delete_message, name='delete_message'),

    # # PDF Document URLs
    # path('pdf/upload/', views.upload_pdf, name='upload_pdf'),
    # path('pdf/<int:pdf_id>/', views.view_pdf, name='view_pdf'),
    # path('pdf/<int:pdf_id>/process/', views.process_pdf, name='process_pdf'),
    # path('pdf/<int:pdf_id>/delete/', views.delete_pdf, name='delete_pdf'),

    # # User History URLs
    # path('user/history/', views.view_history, name='view_history')
]
