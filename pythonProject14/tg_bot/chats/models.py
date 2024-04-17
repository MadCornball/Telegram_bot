from django.db import models

class Chat(models.Model):
    name = models.CharField(max_length=100)
    is_group = models.BooleanField(default=False)  # Добавляем поле is_group

    def __str__(self):
        return self.name
