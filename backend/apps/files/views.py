from rest_framework import viewsets

from files.models import File
from files.serializers import FileSerializer
from core.permissions import IsSubscriber


class FileViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()
    permission_classes = [IsSubscriber]

    # @action('/download')  decorator