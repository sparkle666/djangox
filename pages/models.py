from django.db import models
from accounts.models import CustomUser


class Prompt(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True)
    prompt_text = models.CharField(max_length=300)
    image_url = models.CharField(max_length=200)

    def __str__(self):
        return self.prompt
