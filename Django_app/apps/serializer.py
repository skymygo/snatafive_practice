from rest_framework import serializers
from apps.models import User, Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= [
            'src',
            'share_link',
            'username'
        ]

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)
    acc_type = serializers.IntegerField()
    message = serializers.CharField()

    class Meta:
        model = Message
        fields = [
            'sender',
            'receiver',
            'message'
            'acc_type',
        ]
