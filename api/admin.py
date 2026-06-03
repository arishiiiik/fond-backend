from django.contrib import admin
from django import forms
from .models import (
    Project, ProjectGallery, TeamMember, Document,
    HomePage, Direction, News, FondPage, HistoryItem, Contact,
    HelpSection, HelpCard, Partner, DonationRequest, PartnerRequest, 
    VolunteerRequest, HeroSlide
)


class ProjectGalleryInline(admin.TabularInline):
    model = ProjectGallery
    extra = 1


class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'image_url': forms.URLInput(attrs={'placeholder': 'https://...', 'size': 80}),
        }


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ['title', 'city', 'status', 'order']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectGalleryInline]
    fieldsets = (
        ('Основное', {
            'fields': ('slug', 'title', 'city', 'status', 'order')
        }),
        ('Описание', {
            'fields': ('short_description', 'full_description')
        }),
        ('Детали', {
            'fields': ('date', 'goal', 'beneficiaries')
        }),
        ('Изображение', {
            'fields': ('image', 'image_url'),
            'description': 'Загрузите файл ИЛИ укажите внешнюю ссылку на изображение (рекомендуется)'
        }),
    )


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'order']
    list_editable = ['order']
    fieldsets = (
        ('Основное', {
            'fields': ('name', 'position', 'email', 'phone', 'vk_url', 'order')
        }),
        ('Фото', {
            'fields': ('photo', 'photo_url'),
            'description': 'Загрузите файл ИЛИ укажите внешнюю ссылку (рекомендуется)'
        }),
    )


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ['id', 'hero_title']
    fields = ['hero_title', 'hero_text', 'hero_button_text', 'hero_button_link']


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'description', 'order')
        }),
        ('Иконка', {
            'fields': ('icon', 'icon_url'),
            'description': 'Загрузите файл ИЛИ укажите внешнюю ссылку (рекомендуется)'
        }),
    )


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'order']
    list_editable = ['order']
    list_filter = ['date']
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'description', 'date', 'link', 'order')
        }),
        ('Изображение', {
            'fields': ('image', 'image_url'),
            'description': 'Загрузите файл ИЛИ укажите внешнюю ссылку (рекомендуется)'
        }),
    )


@admin.register(FondPage)
class FondPageAdmin(admin.ModelAdmin):
    list_display = ['id', 'about_text_preview']
    fieldsets = (
        ('Текст', {
            'fields': ('about_text',)
        }),
        ('Изображение', {
            'fields': ('about_image', 'about_image_url'),
            'description': 'Загрузите файл ИЛИ укажите внешнюю ссылку (рекомендуется)'
        }),
    )
    
    def about_text_preview(self, obj):
        return obj.about_text[:50] + '...' if obj.about_text else ''
    about_text_preview.short_description = 'О фонде'


@admin.register(HistoryItem)
class HistoryItemAdmin(admin.ModelAdmin):
    list_display = ['year', 'title', 'side', 'order']
    list_editable = ['order', 'side']
    list_filter = ['year']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['city', 'phone', 'email', 'order']
    list_editable = ['order']


@admin.register(HelpSection)
class HelpSectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(HelpCard)
class HelpCardAdmin(admin.ModelAdmin):
    list_display = ['title', 'button_type', 'order']
    list_editable = ['order']
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'description', 'button_text', 'button_type', 'order')
        }),
        ('Иконка', {
            'fields': ('icon', 'icon_url'),
            'description': 'Загрузите файл ИЛИ укажите внешнюю ссылку (рекомендуется)'
        }),
    )


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'link']
    list_editable = ['order']
    fieldsets = (
        ('Основное', {
            'fields': ('name', 'link', 'order')
        }),
        ('Логотип', {
            'fields': ('logo', 'logo_url'),
            'description': 'Загрузите файл ИЛИ укажите внешнюю ссылку (рекомендуется)'
        }),
    )


@admin.register(DonationRequest)
class DonationRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'amount', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email']
    readonly_fields = ['created_at']


@admin.register(PartnerRequest)
class PartnerRequestAdmin(admin.ModelAdmin):
    list_display = ['organization', 'name', 'phone', 'created_at']
    list_filter = ['created_at']
    search_fields = ['organization', 'name', 'email']
    readonly_fields = ['created_at']


@admin.register(VolunteerRequest)
class VolunteerRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'phone', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'city']
    readonly_fields = ['created_at']


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']
    fieldsets = (
        ('Основное', {
            'fields': ('title', 'text', 'button_text', 'button_link', 'order')
        }),
        ('Фоновое изображение', {
            'fields': ('bg_image', 'bg_image_url'),
            'description': 'Загрузите файл ИЛИ укажите внешнюю ссылку (рекомендуется)'
        }),
    )