from datetime import time
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=100)
    floor_number = models.IntegerField(default=0)
    room_number = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name} on {self.floor_number} in {self.room_number}"


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.title
