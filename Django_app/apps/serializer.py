from rest_framework import serializers
from apps.models import User, Message, RollingPaperBoard
import datetime

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= [
            'id'
            'src',
            'share_link',
            'username'
        ]


class RollingPaperBoardSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    board_image = serializers.IntegerField()
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    created_on = serializers.DateTimeField(read_only=True)
    updated_on = serializers.DateTimeField(read_only=True)
    opened_at = serializers.DateTimeField()

    class Meta:
        model = RollingPaperBoard
        fields = [
            'id',
            'title',
            'board_image',
            'owner',
            'opened_at',
            'created_on',
            'updated_on'
        ]

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)
    acc_type = serializers.IntegerField()
    message = serializers.CharField()

    class Meta:
        model = Message
        fields = [
            'id',
            'sender',
            'receiver',
            'message'
            'acc_type',
        ]
