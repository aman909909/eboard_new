from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import board, list, card

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user = user)
        return user

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = board
        fields = '__all__'

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = list
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = card
        fields = '__all__'
