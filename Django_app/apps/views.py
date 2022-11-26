from django.shortcuts import render

from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.request import Request
from apps.models import User, Message, RollingPaperBoard
from apps.serializer import MessageSerializer, RollingPaperBoardSerializer
from django.http import HttpResponseForbidden, HttpResponseBadRequest

import json

# Create your views here.
class RollingPaperBoardListView(ListModelMixin, CreateModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = RollingPaperBoard.objects
    serializer_class = RollingPaperBoardSerializer

    def list(self, request: Request, *args, **kwargs):
        self.queryset = self.queryset.filter(owner=request.user).order_by('-id')
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        rolling_papers = self.queryset.filter(owner=request.user).all()
        if len(rolling_papers)==5:
            return HttpResponseBadRequest(json.dumps({'msg':'Too many RollingPaperBoard'}), content_type='application/json')
        return super().create(request, *args, **kwargs)

    def patch(self, request: Request, *args, **kwargs):
        return self.update(request, partial=True, *args, **kwargs)

class MessageListView(ListModelMixin, CreateModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Message.objects
    serializer_class = MessageSerializer

    def list(self, request: Request, *args, **kwargs):
        self.queryset = self.queryset.filter(owner=request.user).all()
        return super().list(request, *args, **kwargs)