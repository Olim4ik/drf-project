from core.models import BaseModel
from django.db import models


class Post(BaseModel):
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    def __str__(self) -> str:
        return str(self.title)
    
