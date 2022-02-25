from django.db import models

#data object model
class Books(models.Model):
    title = models.CharField(max_length=128)
    excerpt = models.TextField()

    def __str__(self):
        return self.title
