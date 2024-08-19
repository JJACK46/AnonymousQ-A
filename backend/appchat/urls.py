from django.urls import path
from . import views

urlpatterns = [
    # Role URLs
    path("roles/", views.RoleListCreate.as_view(), name="role-list"),
    path("roles/<int:pk>/", views.RoleDetail.as_view(), name="role-detail"),
    # Room URLs
    path("rooms/", views.RoomListCreate.as_view(), name="class-list"),
    path("rooms/<int:pk>/", views.RoomDetail.as_view(), name="class-detail"),
    # Message URLs
    path("chats/", views.MessageListCreate.as_view(), name="chat-list"),
    path("chats/<int:pk>/", views.MessageDetail.as_view(), name="chat-detail"),
    path(
        "chats/by-room/<int:room_id>/",
        views.MessageByRoomView.as_view(),
        name="chats-by-class",
    ),
]
