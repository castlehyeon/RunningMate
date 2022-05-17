from django.db import models


class Account(models.Model):
    nickname = models.CharField(max_length=20, blank=True)
    exp = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'accounts'
