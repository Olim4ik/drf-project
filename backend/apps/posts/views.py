from rest_framework import viewsets
from posts.models import Post
from posts.serializers import PostSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
