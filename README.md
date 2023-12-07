# 4django
---
## project-level/settings.py
ALLOWED_HOST = ['*']

<!-- Azure CSRF verification faild error: Fix -->
CSRF_TRUSTED_ORIGINS = ['https://'+ os.environ['ajsample1.azurewebsites.net']]

---
requirements.txt:
django==4.1
whitenoise
psycopg2-binary

## Commands:
python -c "import django; print(django.get_version())"
4.1

python --version
Python 3.11.5

---