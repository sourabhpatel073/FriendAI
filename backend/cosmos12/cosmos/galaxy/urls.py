from django.urls import path
from . import views
from .views import get_all_chats, create_chat, get_chat, update_chat, delete_chat
urlpatterns = [

    path('chat/', get_all_chats, name='get-all-chats'),
    path('chat/create/', create_chat, name='create-chat'),
    path('chat/<int:pk>/', get_chat, name='get-chat'),
    path('chat/update/<int:pk>/', update_chat, name='update-chat'),
    path('chat/delete/<int:pk>/', delete_chat, name='delete-chat'),



    # User Profile URLs
    path('user_register/', views.register_user, name='register_user'),
    path('user_login/', views.login_user, name='login_user'),
    path('user/edit/<int:user_id>/', views.edit_user_profile, name='edit_user_profile'),
    path('user/delete/', views.delete_user_profile, name='delete_user_profile'),
    path('get-all-users/', views.get_all_users, name='get-all-users'),
    path('get_profile/<int:user_id>/', views.get_profile, name='get-profile'),

    path('upload_pdfs/', views.upload_pdfs, name='upload_pdfs'),
    path('ask_question/', views.ask_question, name='ask_question'),

    
    path('ask/', views.ask, name='ask'),
    path('generate-image/', views.generate_image, name='generate_image'),
]
