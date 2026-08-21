from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Automatically creates a superuser if it does not exist"

    def handle(self, *args, **options):
        User = get_user_model()

        username = "sodiqadmin"
        email = "sannisodiq031@gmail.com"
        password = "Ishola@031"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS("✅ Superuser created successfully!"))
        else:
            self.stdout.write(self.style.WARNING("⚠️ Superuser already exists."))



