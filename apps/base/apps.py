"""Base application"""
from django.apps import AppConfig


class BaseConfig(AppConfig):
    """Base configuration"""
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.base"
