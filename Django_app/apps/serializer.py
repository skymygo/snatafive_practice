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
    link = serializers.CharField(read_only=True, required=False)

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
    sender = serializers.HiddenField(default=serializers.CurrentUserDefault())
    acc_type = serializers.IntegerField()
    contents = serializers.CharField()
    rolling_paper_board = RollingPaperBoardSerializer(read_only=True)
    link = serializers.CharField(write_only=True)

    def create(self, validated_data):
        validated_data['rolling_paper_board'] = RollingPaperBoard.objects.filter(link=validated_data['link']).first()
        del validated_data['link']
        message = Message.objects.create(**validated_data)
        return message


    class Meta:
        model = Message
        fields = [
            'id',
            'sender',
            'contents',
            'acc_type',
            'rolling_paper_board',
            'link'
        ]
