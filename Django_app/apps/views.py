from django.shortcuts import render

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.request import Request
from apps.models import User, Message
from apps.serializer import MessageSerializer

# Create your views here.
class RollingPaperBoardListView(ListModelMixin, CreateModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = Message.objects.order_by("-id")
    serializer_class = MessageSerializer

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def patch(self, request: Request, *args, **kwargs):
        return self.update(request, partial=True, *args, **kwargs)