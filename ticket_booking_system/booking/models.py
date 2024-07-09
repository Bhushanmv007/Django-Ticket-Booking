from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    buyer_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} tickets for {self.event.name}"
