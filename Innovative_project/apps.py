from django.apps import AppConfig


class InnovativeProjectConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Innovative_project"

    def ready(self):
        pass
