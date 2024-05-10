from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from Innovative_project.models import Host
from Innovative_project.serializers import (
    HostSerializer,
    UserSerializer,
)


@authentication_classes([JWTAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated, IsAdminUser])
class UserView(viewsets.ModelViewSet):
    prefix = "users"
    lookup_field = "id"
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)


@authentication_classes([JWTAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class ReadOnlyHostView(viewsets.ReadOnlyModelViewSet):
    prefix = "hosts"
    lookup_field = "id"
    queryset = Host.objects.all()
    serializer_class = HostSerializer
    filter_backends = (DjangoFilterBackend,)


@authentication_classes([JWTAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class WriteOnlyHostView(CreateModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    prefix = "hosts"
    lookup_field = "id"
    queryset = Host.objects.all()
    serializer_class = HostSerializer
    filter_backends = (DjangoFilterBackend,)
