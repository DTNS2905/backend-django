from rest_framework import serializers

from Innovative_project.models import BlogPost
from Innovative_project.users.models import User
from Innovative_project.hosts.models import Host


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ["id", "title", "content", "published_date"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Include all fields by default (adjust as needed)


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = '__all__'
