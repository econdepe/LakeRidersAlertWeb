from django.db import models


class Session(models.Model):
    datetime = models.DateTimeField("session date")
    members = models.CharField("session members", max_length=200)


class Alert(models.Model):
    calendar_entry = models.ForeignKey(Session, on_delete=models.PROTECT)
    timestamp = models.PositiveIntegerField("alert UNIX timestamp")
    count = models.PositiveSmallIntegerField("number of free slots")
    members = models.CharField("members dropped", max_length=200)
