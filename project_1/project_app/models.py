from django.db import models

class Users(models.Model):

    username = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    id_group_user = models.CharField(max_length=100)
    audit_date = models.DateTimeField()
    audit_user = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username}"

    class Meta:
        db_table = 'r_user'