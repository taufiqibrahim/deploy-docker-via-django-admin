from django.db import models

class Container(models.Model):
    container_host = models.URLField()
    container_port = models.PositiveIntegerField()
    container_default_message = models.CharField(
        max_length=255
    )
