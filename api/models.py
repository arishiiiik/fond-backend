from django.db import models


# ========== ПРОЕКТЫ ==========
class Project(models.Model):
    STATUS_CHOICES = [
        ("active", "Активный"),
        ("completed", "Завершён"),
        ("annual", "Ежегодный"),
    ]

    slug = models.SlugField(unique=True, primary_key=True, max_length=100)
    title = models.CharField(max_length=200, verbose_name="Название")
    city = models.CharField(max_length=200, verbose_name="Локация")
    short_description = models.TextField(verbose_name="Краткое описание")
    full_description = models.TextField(blank=True, verbose_name="Полное описание")
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="active", verbose_name="Статус"
    )
    date = models.CharField(max_length=100, verbose_name="Сроки")
    goal = models.TextField(blank=True, verbose_name="Цель")
    beneficiaries = models.CharField(
        max_length=200, blank=True, verbose_name="Бенефициары"
    )
    image = models.ImageField(
        upload_to="projects/", null=True, blank=True, verbose_name="Изображение"
    )
    order = models.IntegerField(default=0, verbose_name="Порядок")

    class Meta:
        ordering = ["order"]
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.title


class ProjectGallery(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="gallery"
    )
    image = models.ImageField(upload_to="projects/gallery/")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]


# ========== КОМАНДА ==========
class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    vk_url = models.URLField(blank=True)
    photo = models.ImageField(upload_to="team/", null=True, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]


# ========== ДОКУМЕНТЫ ==========
class Document(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="documents/")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]


# ========== ГЛАВНАЯ СТРАНИЦА ==========
class HomePage(models.Model):
    hero_title = models.CharField(
        max_length=200, default="Развиваем малые города и сёла Вологодской области"
    )
    hero_text = models.TextField(
        default="Создаём условия для устойчивого развития территорий через комплексные программы поддержки"
    )
    hero_button_text = models.CharField(max_length=100, default="Узнать о проектах")
    hero_button_link = models.CharField(max_length=200, default="/projects")

    class Meta:
        verbose_name = "Главная страница"
        verbose_name_plural = "Главная страница"


class Direction(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to="directions/", blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]


class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to="news/", blank=True, null=True)
    link = models.URLField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["-date"]


# ========== СТРАНИЦА "О ФОНДЕ" ==========
class FondPage(models.Model):
    about_text = models.TextField()
    about_image = models.ImageField(upload_to="fond/", blank=True, null=True)

    class Meta:
        verbose_name = "О фонде"
        verbose_name_plural = "О фонде"


class HistoryItem(models.Model):
    year = models.IntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    side = models.CharField(
        max_length=10, choices=[("left", "Слева"), ("right", "Справа")], default="left"
    )
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]


# ========== КОНТАКТЫ ==========
class Contact(models.Model):
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    vk_url = models.URLField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]


# ========== БЛОК ПОМОЩИ ==========
class HelpSection(models.Model):
    title = models.CharField(max_length=200, default="Как помочь фонду?")
    description = models.TextField(
        default="Вы можете внести вклад в развитие малых городов и сёл Вологодской области"
    )

    class Meta:
        verbose_name = "Блок помощи"
        verbose_name_plural = "Блок помощи"


class HelpCard(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to="help/", blank=True, null=True)
    button_text = models.CharField(max_length=100, default="Поддержать")
    button_type = models.CharField(max_length=50, default="donation")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]

    # models.py


class Partner(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    logo = models.ImageField(
        upload_to="partners/", blank=True, null=True, verbose_name="Логотип"
    )
    link = models.URLField(blank=True, verbose_name="Сайт")
    order = models.IntegerField(default=0, verbose_name="Порядок")

    class Meta:
        ordering = ["order"]
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"
class DonationRequest(models.Model):
    """Заявка на пожертвование"""
    name = models.CharField(max_length=200, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email", blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Заявка на пожертвование"
        verbose_name_plural = "Заявки на пожертвования"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.amount} ₽"


class PartnerRequest(models.Model):
    """Заявка на партнёрство"""
    name = models.CharField(max_length=200, verbose_name="Имя")
    position = models.CharField(max_length=200, blank=True, verbose_name="Должность")
    organization = models.CharField(max_length=200, verbose_name="Организация")
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Заявка на партнёрство"
        verbose_name_plural = "Заявки на партнёрства"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.organization} - {self.name}"


class VolunteerRequest(models.Model):
    """Заявка волонтёра"""
    name = models.CharField(max_length=200, verbose_name="Имя")
    age = models.IntegerField(null=True, blank=True, verbose_name="Возраст")
    city = models.CharField(max_length=200, verbose_name="Город")
    phone = models.CharField(max_length=50, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Заявка волонтёра"
        verbose_name_plural = "Заявки волонтёров"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.city}"
    
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(is_superuser=True).exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')