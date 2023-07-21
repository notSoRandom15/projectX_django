from django.db import models
from PIL import Image

class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.cover.path)

        max_width = 800
        max_height = 600

        img.thumbnail((max_width, max_height))

        img.save(self.cover.path, optimize=True)