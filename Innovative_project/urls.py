from django.urls import path, include
from rest_framework_nested import routers
from Innovative_project.views import UserView, ReadOnlyHostView, WriteOnlyHostView

user_router = routers.SimpleRouter()
user_router.register(UserView.prefix, UserView, basename="Users")

read_host_router = routers.SimpleRouter()
read_host_router.register(ReadOnlyHostView.prefix, ReadOnlyHostView, basename="ReadOnlyHostView")

write_host_router = routers.SimpleRouter()
write_host_router.register(WriteOnlyHostView.prefix, WriteOnlyHostView, basename="WriteOnlyHostView")

urlpatterns = [
    path(r"",  include(user_router.urls)),
    path(r"",  include(read_host_router.urls)),
    path(r"",  include(write_host_router.urls))
]
