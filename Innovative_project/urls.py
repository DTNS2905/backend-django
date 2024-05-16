from django.urls import path, include
from rest_framework_nested import routers
from Innovative_project.views import (UserView,
                                      ReadOnlyHostView, WriteOnlyHostView, ReadOnlyContractView, WriteOnlyContractView,
                                      EquipmentView, BillView, RoomView, ServiceView)

user_router = routers.SimpleRouter()
user_router.register(UserView.prefix, UserView, basename="Users")

read_host_router = routers.SimpleRouter()
read_host_router.register(ReadOnlyHostView.prefix, ReadOnlyHostView, basename="ReadOnlyHostView")

write_host_router = routers.SimpleRouter()
write_host_router.register(WriteOnlyHostView.prefix, WriteOnlyHostView, basename="WriteOnlyHostView")

read_contract_router = routers.SimpleRouter()
read_contract_router.register(ReadOnlyContractView.prefix, ReadOnlyContractView, basename="ReadOnlyContractView")

write_contract_router = routers.SimpleRouter()
write_contract_router.register(WriteOnlyContractView.prefix, WriteOnlyContractView, basename="WriteOnlyContractView")

equipment_router = routers.SimpleRouter()
equipment_router.register(EquipmentView.prefix, EquipmentView, basename="EquipmentView")

bill_router = routers.SimpleRouter()
bill_router.register(BillView.prefix, BillView, basename="BillView")

room_router = routers.SimpleRouter()
room_router.register(RoomView.prefix, RoomView, basename="RoomView")

service_router = routers.SimpleRouter()
service_router.register(ServiceView.prefix, ServiceView, basename="ServiceView")

urlpatterns = [
    path(r"", include(user_router.urls)),
    path(r"", include(read_host_router.urls)),
    path(r"", include(write_host_router.urls)),
    path(r"", include(read_contract_router.urls)),
    path(r"", include(write_contract_router.urls)),
    path(r"", include(equipment_router.urls)),
    path(r"", include(bill_router.urls)),
    path(r"", include(room_router.urls)),
    path(r"", include(service_router.urls)),
]
