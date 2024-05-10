from django.views.generic import CreateView
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.urls import reverse_lazy

from Innovative_project.models import BlogPost
from Innovative_project.serializers import UserSerializer, BlogPostSerializer, HostSerializer
from Innovative_project.users.models import User
from Innovative_project.hosts.models import Host


# create post
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# update and delete Post
class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"


class BlogPostList(APIView):
    def get(self, request, format=None):
        # get the title from query parameters(if none, default to empty string)
        title = request.query_params.get("title", "")

        if title:
            # Filter the queryset based on the title
            blog_posts = BlogPost.objects.filter(title__icontains=title)
        else:
            # if no title is provided,return all blog posts
            blog_posts = BlogPost.objects.all()

        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data, status=status.HTTTP_200_ok)


def create_user(username, password, email, host_id, phone, is_active=True):
    # Your custom user creation logic (e.g., additional field validation)
    user = User.objects.create_user(username, email, phone, host_id, password, is_active=is_active)
    user.save()
    return user


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # permission_classes = [IsAuthenticated]  # Optional permission for authenticated users

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            print(serializer.data)
            # Use your custom user creation function
            user = create_user(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password'],
                email=serializer.validated_data['email'],
                host_id=serializer.validated_data['host_id'],
                phone=serializer.validated_data['phone'],
                is_active=serializer.validated_data.get('is_active', True),  # Optional: Use .get() for default value
            )
            # Optionally send a welcome email or perform other actions

            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # permission_classes = [IsAuthenticated]  # Optional permission for access control

    def get_object(self):
        # You can customize object retrieval logic here (e.g., handle permission checks)
        pk = self.kwargs['pk']
        return self.get_queryset().get(pk=pk)


class HostListCreateAPIView(APIView):
    # permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        """
        Retrieve a list of all hosts.
        """
        hosts = Host.objects.all()
        serializer = HostSerializer(hosts, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new host.
        """
        serializer = HostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # CREATED status code
        return Response(serializer.errors, status=400)  # BAD REQUEST status code


class HostCreate(generics.ListCreateAPIView):
    queryset = Host.objects.all()
    serializer_class = HostSerializer

    def delete(self, request, *args, **kwargs):
        Host.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)