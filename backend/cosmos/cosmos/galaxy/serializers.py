from django.contrib.auth.models import User
from.models import Chat, Message, PDFDocument,UserHistory,UserProfile
from rest_framework import serializers



from .models import UserChatHistory

class UserChatHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChatHistory
        fields = '__all__'



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [ 'join_date', "profile_picture"]

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'userprofile']

    def create(self, validated_data):
        profile_data = validated_data.pop('userprofile')
        user = User.objects.create(**validated_data)
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        # Handle the nested UserProfile
        profile_data = validated_data.pop('userprofile')
        profile_instance = instance.userprofile

        # Update user instance
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        # Update user profile instance
        profile_instance.join_date = profile_data.get('join_date', profile_instance.join_date)
        
        # Here's the modification to handle profile_pic
        profile_instance.profile_picture = profile_data.get('profile_picture', profile_instance.profile_picture)

        profile_instance.save()

        return instance



class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'participants', 'timestamp']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'content', 'timestamp', 'attachments']

class PDFDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDFDocument
        fields = ['id', 'title', 'uploaded_by', 'upload_date', 'embedding']


class UserHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserHistory
        fields = ['id', 'user', 'action', 'timestamp']