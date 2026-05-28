from django.contrib import admin
from .models import (
    Project, ProjectGallery, TeamMember, Document,
    HomePage, Direction, News, FondPage, HistoryItem, Contact,
    HelpSection, HelpCard, Partner, DonationRequest, PartnerRequest, VolunteerRequest
)

class ProjectGalleryInline(admin.TabularInline):
    model = ProjectGallery
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'city', 'status', 'order']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectGalleryInline]

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'order']
    list_editable = ['order']

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']

# ========== ДОБАВЬТЕ ЭТИ КЛАССЫ ==========

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ['id', 'hero_title']
    fields = ['hero_title', 'hero_text', 'hero_button_text', 'hero_button_link']

@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'order']
    list_editable = ['order']
    list_filter = ['date']

@admin.register(FondPage)
class FondPageAdmin(admin.ModelAdmin):
    list_display = ['id', 'about_text_preview']
    
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

# Если есть модель Partner
@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'link']
    list_editable = ['order']

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