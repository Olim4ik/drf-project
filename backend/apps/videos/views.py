# from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
# from rest_framework.response import Response
from rest_framework import status
from videos.models import Video
from .serializers import VideoSerializer


class VideoViewSet(ReadOnlyModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
    
    # def get(self, request):
    #     return Response({'videos': []}, status=status.HTTP_200_OK)



