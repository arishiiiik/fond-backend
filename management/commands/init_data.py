# fond/management/commands/init_data.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from fond.models import HomePage, FondPage, HelpSection, Direction, News, Contact, HistoryItem, HelpCard

class Command(BaseCommand):
    help = 'Initialize default data for the site'

    def handle(self, *args, **kwargs):
        # Создаем HomePage если нет
        if not HomePage.objects.exists():
            HomePage.objects.create(
                hero_title="Развиваем малые города и сёла Вологодской области",
                hero_text="Создаём условия для устойчивого развития территорий через комплексные программы поддержки",
                hero_button_text="Узнать о проектах",
                hero_button_link="/projects"
            )
            self.stdout.write(self.style.SUCCESS('HomePage created'))

        # Создаем FondPage если нет
        if not FondPage.objects.exists():
            FondPage.objects.create(
                about_text="Фонд 'Земля Вологодская' создан для поддержки и развития малых территорий...",
                about_image=None
            )
            self.stdout.write(self.style.SUCCESS('FondPage created'))

        # Создаем HelpSection если нет
        if not HelpSection.objects.exists():
            HelpSection.objects.create(
                title="Как помочь фонду?",
                description="Вы можете внести вклад в развитие малых городов и сёл Вологодской области"
            )
            self.stdout.write(self.style.SUCCESS('HelpSection created'))

        # Создаем тестовые направления
        if not Direction.objects.exists():
            directions = [
                {"title": "Образование", "description": "Поддержка образовательных программ", "order": 1},
                {"title": "Культура", "description": "Развитие культурных проектов", "order": 2},
                {"title": "Экология", "description": "Защита окружающей среды", "order": 3},
            ]
            for dir_data in directions:
                Direction.objects.create(**dir_data)
            self.stdout.write(self.style.SUCCESS('Directions created'))

        # Создаем тестовые контакты
        if not Contact.objects.exists():
            contacts = [
                {
                    "city": "Вологда",
                    "address": "г. Вологда, ул. Ленина, 1",
                    "phone": "+7 (8172) 00-00-00",
                    "email": "vologda@fond.ru",
                    "order": 1
                },
                {
                    "city": "Череповец",
                    "address": "г. Череповец, пр. Победы, 10",
                    "phone": "+7 (8202) 00-00-00",
                    "email": "cherepovets@fond.ru",
                    "order": 2
                },
            ]
            for contact in contacts:
                Contact.objects.create(**contact)
            self.stdout.write(self.style.SUCCESS('Contacts created'))

        self.stdout.write(self.style.SUCCESS('Initial data created successfully!'))