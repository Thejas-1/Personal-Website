from django.db import models

class Post(models.Model):
    def publish(self):
	self.save()

    def __str__(self):
        return self.title

# Create your models here.
