from django.urls import include, path
from rest_framework import routers
from .views import EducationViewSet, WorkViewSet, ResearchViewSet, GalleryViewSet

router = routers.DefaultRouter()
router.register('education', EducationViewSet)
router.register('work', WorkViewSet)
router.register('research', ResearchViewSet)
router.register('gallery', GalleryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]