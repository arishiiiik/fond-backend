import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import Project

projects_data = [
    {'slug': 'sady-severa', 'title': 'Сады Севера', 'city': 'Кирилловский район', 'short_description': 'Испытание сортов плодовых и декоративных растений', 'status': 'active', 'date': 'Актуально сейчас', 'order': 1},
    {'slug': 'usadba-spasskoe-kurkino', 'title': 'Усадьба Спасское-Куркино', 'city': 'Вологодский район', 'short_description': 'Создание модели современной усадьбы', 'status': 'active', 'date': '2024 - 2025', 'order': 2},
    # добавь остальные проекты
]

for data in projects_data:
    obj, created = Project.objects.update_or_create(slug=data['slug'], defaults=data)
    print(f'{"Создан" if created else "Обновлён"}: {obj.title}')