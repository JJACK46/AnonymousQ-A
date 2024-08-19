from django.shortcuts import render
from rest_framework import generics
from .models import Role, Room, Message
from .serializers import RoleSerializer, RoomSerializer, MessageSerializer

# Create your views here.


# Role Views
class RoleListCreate(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class RoleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


# Room Views
class RoomListCreate(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


# Message Views
class MessageListCreate(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageByRoomView(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        class_id = self.kwargs["class_id"]
        return Message.objects.filter(class_id=class_id)
