import os
from django.contrib.auth import get_user_model

User = get_user_model()

# Informações do superusuário padrão
ADMIN_USERNAME = os.getenv("DJANGO_ADMIN_USERNAME", "admin@problemz.com")
ADMIN_EMAIL = os.getenv("DJANGO_ADMIN_EMAIL", "admin@problemz.com")
ADMIN_PASSWORD = os.getenv("DJANGO_ADMIN_PASSWORD", "admin123")

# Verifica se o superusuário já existe
if not User.objects.filter(username=ADMIN_USERNAME).exists():
    print("Criando superusuário padrão...")
    User.objects.create_superuser(
        username=ADMIN_USERNAME,
        email=ADMIN_EMAIL,
        password=ADMIN_PASSWORD,
        first_name="Admin",
        last_name="Problemz"
    )
    print(f"Superusuário '{ADMIN_USERNAME}' criado com sucesso!")
else:
    print(f"Superusuário '{ADMIN_USERNAME}' já existe.")
