from django.shortcuts import redirect
from .models import User
from .serializers import UserDetailSerializer
from rest_framework import permissions, viewsets
from djoser.views import UserViewSet
import os

FrontEndUrl = os.environ.get('FRONT_END_URL')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()[:1]
    serializer_class = UserDetailSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]




def RedirectView(self, uid, token):
    return redirect(f'{FrontEndUrl}password/reset/confirm/{uid}/{token}/')
