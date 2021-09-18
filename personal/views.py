from rest_framework import viewsets, permissions
from .models import Education, Work, Research, Gallery
from .serializers import EducationSerializer, WorkSerializer, ResearchSerializer, GallerySerializer


class EducationViewSet(viewsets.ModelViewSet):
    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Education.objects.all()


class WorkViewSet(viewsets.ModelViewSet):
    serializer_class = WorkSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Work.objects.all()


class ResearchViewSet(viewsets.ModelViewSet):
    serializer_class = ResearchSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Research.objects.all()


class GalleryViewSet(viewsets.ModelViewSet):
    serializer_class = GallerySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Gallery.objects.all()
