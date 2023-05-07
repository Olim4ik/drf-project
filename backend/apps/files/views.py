from rest_framework import viewsets

from files.models import File
from files.serializers import FileSerializer


class FileViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()

    # @action('/download')  decorator