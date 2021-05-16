from django.db import models


# Create your models here.
class entry(models.Model):
    entry_title = models.CharField(max_length=200)
    entry_date = models.DateTimeField('date published')
    entry_body = models.TextField()

    def __str__(self):
        return self.entry_title
