from rest_framework import serializers

from Innovative_project.models import Host
from Innovative_project.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"  # Include all fields by default (adjust as needed)


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = "__all__"
