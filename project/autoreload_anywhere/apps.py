from django.apps import AppConfig


class AutoreloadAnywhereConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "autoreload_anywhere"

    def ready(self) -> None:
        import asyncio
        from .utils import reload_webapp
        return super().ready()
