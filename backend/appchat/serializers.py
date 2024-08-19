from rest_framework import serializers
from .models import Role, Room, Message


# Role Serializer
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


# Room Serializer
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


# Message Serializer
class MessageSerializer(serializers.ModelSerializer):
    classId = serializers.PrimaryKeyRelatedField(
        queryset=Room.objects.all(), source="room_id"
    )
    roleId = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(), source="role_id"
    )

    class Meta:
        model = Message
        fields = ["id", "text", "roomId", "roleId"]
