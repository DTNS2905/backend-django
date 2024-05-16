from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from Innovative_project.models import Host, Contract, Equipment, EquipmentContract, Service, Room, Bill
from Innovative_project.serializers import (
    HostSerializer,
    UserSerializer,
    ContractSerializer,
    EquipmentSerializer,
    EquipmentContractSerializer, ServiceSerializer, RoomSerializer, BillSerializer,
)
from core.pagination.pagination import BaseResultsSetPagination


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


@authentication_classes([JWTAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class ReadOnlyContractView(viewsets.ModelViewSet):
    prefix = "contracts"
    lookup_field = "id"
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    filter_backends = (DjangoFilterBackend,)


@authentication_classes([JWTAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class WriteOnlyContractView(CreateModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    prefix = "contracts"
    lookup_field = "id"
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    filter_backends = (DjangoFilterBackend,)


@authentication_classes([JWTAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class EquipmentView(viewsets.ModelViewSet):
    prefix = "Equipments"
    lookup_field = "id"
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    filter_backends = (DjangoFilterBackend,)


@authentication_classes([JWTAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class EquipmentView(viewsets.ModelViewSet):
    prefix = "Equipments_Contracts"
    lookup_field = "id"
    queryset = EquipmentContract.objects.all()
    serializer_class = EquipmentContractSerializer
    filter_backends = (DjangoFilterBackend,)


@authentication_classes([JWTAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class ServiceView(viewsets.ModelViewSet):
    prefix = "Services"
    lookup_field = "id"
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = BaseResultsSetPagination
    filter_backends = (DjangoFilterBackend,)


@authentication_classes([JWTAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class RoomView(viewsets.ModelViewSet):
    prefix = "Rooms"
    lookup_field = "id"
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    pagination_class = BaseResultsSetPagination
    filter_backends = (DjangoFilterBackend,)


@authentication_classes([JWTAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class BillView(viewsets.ModelViewSet):
    prefix = "Bills"
    lookup_field = "id"
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    pagination_class = BaseResultsSetPagination
    filter_backends = (DjangoFilterBackend,)
