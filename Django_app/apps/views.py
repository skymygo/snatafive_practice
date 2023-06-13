from django.shortcuts import render

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin
from rest_framework.request import Request
from rest_framework.response import Response

from apps.models import User, Message, RollingPaperBoard
from apps.serializer import MessageSerializer, RollingPaperBoardSerializer
from django.http import HttpResponseForbidden, HttpResponseBadRequest
from django.db.models import Q, Prefetch

import json, datetime

# Create your views here.
class RollingPaperBoardListView(ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = RollingPaperBoard.objects.prefetch_related(
            Prefetch(
                "rolling_paper_board_message_set"
            )
        )
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

    def retrieve(self, request, *args, **kwargs):
        rolling_paper = self.get_object()
        serializer = self.get_serializer(rolling_paper)
        data = serializer.data
        if datetime.datetime.now(tz=datetime.timezone.utc) < data['opened_at']:
            for message in data['messages']:
                message['contents'] = 'wait'
        return Response(serializer.data)


class MessageListView(ListModelMixin, CreateModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Message.objects
    serializer_class = MessageSerializer

    def list(self, request: Request, *args, **kwargs):
        self.queryset = self.queryset.filter(sender=request.user).all()
        return super().list(request, *args, **kwargs)