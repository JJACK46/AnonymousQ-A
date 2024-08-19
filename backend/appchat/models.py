from django.db import models

# Create your models here.


# Role Entity
class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Room Entity
class Room(models.Model):
    name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Message Entity
class Message(models.Model):
    text = models.TextField()
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="chats")
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="chats")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat in {self.room_id.name} by {self.role_id.name}"
