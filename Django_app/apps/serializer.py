from rest_framework import serializers
from apps.models import User, Message, RollingPaperBoard
from django.db import transaction
import hashlib, datetime, time

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
    link = serializers.HiddenField(default=None)

    def create(self, validated_data):
        hash_str = f"{validated_data['owner']}_{validated_data['title']}_{time.time()}".encode('utf-8')
        validated_data['link'] = hashlib.sha256(hash_str).hexdigest()
        rollingpaper = RollingPaperBoard.objects.create(**validated_data)
        return rollingpaper

    class Meta:
        model = RollingPaperBoard
        fields = [
            'id',
            'title',
            'board_image',
            'owner',
            'opened_at',
            'created_on',
            'updated_on',
            'link'
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
