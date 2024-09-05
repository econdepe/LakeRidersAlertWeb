from django.db import models


class Session(models.Model):
    datetime = models.CharField("session date", max_length=13)
    members = models.CharField("session members", max_length=200)


class Alert(models.Model):
    session = models.ForeignKey(Session, on_delete=models.PROTECT)
    timestamp = models.PositiveIntegerField("alert UNIX timestamp")
    count = models.PositiveSmallIntegerField("number of free slots")
    # members = models.CharField("members dropped", max_length=200)
