from core.models import BaseModel, BaseImage
from django.db import models
from ckeditor.fields import RichTextField


class Post(BaseModel):
    title = models.CharField(max_length=255, blank=True)
    body = RichTextField()  # TextField()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    def __str__(self) -> str:
        return str(self.title)
    

class PostImage(BaseImage):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
