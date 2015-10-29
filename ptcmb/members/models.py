from django.db import models

class MemberData(models.Model):
    coins = models.IntegerField(default=0)
    posts = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    name = models.CharField(max_length=40, default="")

    def __str__(self):
        return self.name
