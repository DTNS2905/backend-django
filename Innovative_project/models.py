import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinValueValidator
from django.db import models
from django.template.defaultfilters import slugify
from Innovative_project.constants import Condition, Status, RoomStatus, RoomTypes
from django.utils.translation import gettext_lazy as _

from Innovative_project.managers import UserManager


class Host(models.Model):
    hostname = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, unique=True, blank=True)
    email = models.EmailField(max_length=255, unique=True, blank=True)

    def __str__(self):
        return self.hostname


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=100, unique=True
    )  # Assuming username is unique
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=20, unique=True)  # Assuming phone is unique
    host = models.ForeignKey(
        Host, on_delete=models.CASCADE, default=1
    )  # Update the reference

    USERNAME_FIELD = "username"  # Use username for user login
    REQUIRED_FIELDS = ["email", "phone"]

    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # A flag for staff accounts
    is_superuser = models.BooleanField(default=False)  # A flag for superusers

    def __str__(self):
        return self.username


class ContractRepresentation:
    def __init__(self, contract):
        self.contract = contract

    def __str__(self):
        return _("Contract for %(host)s and %(user)s") % {
            'host': self.contract.host,
            'user': self.contract.user,
        }


class Contract(models.Model):
    host = models.ForeignKey(
        Host, on_delete=models.CASCADE, default=1
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1
    )
    deposit = models.DecimalField(max_digits=10, decimal_places=2, blank=False)  # Represent deposit as currency
    date_of_contract = models.DateField(default=datetime.date.today)  # Capture date contract is created
    check_in_date = models.DateField(blank=True, null=True)
    check_out_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(ContractRepresentation(self))


class Equipment(models.Model):
    name = models.CharField(max_length=255)  # Optional, more user-friendly name
    type = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    model_number = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255)
    # Inventory and status tracking
    condition = models.CharField(max_length=50, choices=Condition, default="Good")
    # Dates
    date_acquired = models.DateField(blank=True, null=True)
    warranty_expiry = models.DateField(blank=True, null=True)
    purchase_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    maintenance_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    contracts = models.ManyToManyField(Contract, through="EquipmentContract", through_fields=('equipment', 'contract'))

    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.model_number)  # Or any other field for slug creation
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class EquipmentContract(models.Model):
    contract = models.ForeignKey(
        Contract, on_delete=models.CASCADE, default=1
    )
    equipment = models.ForeignKey(
        Equipment, on_delete=models.CASCADE, default=1
    )


class Service(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    available_time = models.DateField(blank=True, null=True)
    Status = models.CharField(max_length=50, choices=Status, default="Available")
    contracts = models.ManyToManyField(Contract, through="ServiceContract", through_fields=('service', 'contract'))


class ServiceContract(models.Model):
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, default=1
    )
    contract = models.ForeignKey(
        Contract, on_delete=models.CASCADE, default=1
    )


class Bill(models.Model):
    contract = models.ForeignKey(
        Contract, on_delete=models.CASCADE, default=1
    )
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    settlement_date = models.DateField(blank=True, null=True)
    management_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    additional_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.management_fee is not None and self.additional_fee is not None and self.total is None:
            self.total = self.management_fee + self.additional_fee
        else:
            self.total = self.total
        super().save(*args, **kwargs)


class Room(models.Model):
    type = models.CharField(max_length=50, choices=RoomTypes, default="Single")
    area_size = models.DecimalField(max_digits=10, decimal_places=2, default=10, validators=[MinValueValidator(0)])
    number_of_kitchens = models.PositiveIntegerField(default=1)
    number_of_bathrooms = models.PositiveIntegerField(default=1)
    number_of_beds = models.PositiveIntegerField(default=1)
    number = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    status = models.CharField(max_length=50, choices=RoomStatus, default="Available")
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE, primary_key=False, default=1)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Room ({self.number})"
