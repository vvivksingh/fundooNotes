from rest_framework import serializers
from .models import NotesUser


class NotesUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotesUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'mobile', 'age']


class NotesUserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        models = NotesUser
        fields = ['username', 'password']
