from django.db import models

from blog.validators import validate_title_length, validate_caption_length


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=36, validators=[validate_title_length])
    caption = models.TextField(validators=[validate_caption_length])

    def __str__(self):
        return f'{self.title}'
