from django.urls import path
from django.contrib import admin
from Innovative_project import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('hosts/', views.HostCreate.as_view()),
    path('admin/', admin.site.urls),
]