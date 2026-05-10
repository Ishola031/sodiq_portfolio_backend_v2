from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Project, Service


@receiver([post_delete,post_save], sender=Project)
def clear_project_cache(sender, **Kwargs):
    cache.delete_pattern("views.decorators.cache*")


@receiver([post_delete,post_save], sender=Service)
def clear_service_cache(sender, **Kwargs):
    cache.delete_pattern("views.decorators.cache*")