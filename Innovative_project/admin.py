from django.contrib import admin

from Innovative_project.models import User, Host, Contract, Equipment, EquipmentContract, Bill, Room, Service


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "phone",
        "host",
    )


@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    list_display = (
        "hostname",
        "address",
        "phone",
        "email",
    )


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = (
        "host",
        "user",
        "deposit",
        "date_of_contract",
        "check_in_date",
        "check_out_date",
    )


class EquipmentContractInline(admin.TabularInline):
    def __init__(self, parent_model, admin_site):
        super().__init__(parent_model, admin_site)
        self.forms = None

    model = EquipmentContract
    fields = ["contract", "equipment"]


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "type",
        "brand",
        "model_number",
        "serial_number",
        "condition",
        "date_acquired",
        "warranty_expiry",
        "purchase_cost",
        "maintenance_cost",
    )
    inlines = [
        EquipmentContractInline,

    ]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        equipment_instance = form.instance
        for formset in formsets:
            if isinstance(formset, EquipmentContractInline):
                for inline_form in formset.forms:
                    if inline_form.instance.pk is None:
                        # If it's a new EquipmentContract instance, connect it to the current Equipment instance
                        inline_form.instance.equipment = equipment_instance
                        inline_form.instance.save()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "number",
        "status",
        "description",
        "contract"
    )


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = (
        "additional_fee",
        "management_fee",
        "settlement_date",
        "total",
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "type",
        "available_time",
        "Status",
    )
