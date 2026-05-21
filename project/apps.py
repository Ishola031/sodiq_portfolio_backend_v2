from django.apps import AppConfig
from django.db.models.signals import post_migrate

def create_admin_superuser(sender, **kwargs):
    # This prevents the signal from running recursively on other apps
    if sender.name == 'project': 
        from django.contrib.auth import get_user_model
        User = get_user_model()

        username = "sodiqadmin"
        email = "sannisodiq031@gmail.com"
        password = "Ishola@031"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            print("✅ Superuser created successfully via post_migrate signal!")
        else:
            print("⚠️ Superuser already exists.")


class ProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'project'

    def ready(self):
        post_migrate.connect(create_admin_superuser, sender=self)
        import project.signals