from rest_framework import serializers
from .models import (
    Project, ProjectGallery, TeamMember, Document,
    HomePage, Direction, News, FondPage, HistoryItem, Contact,
    HelpSection, HelpCard, Partner,
    DonationRequest, PartnerRequest, VolunteerRequest
)


class PartnerSerializer(serializers.ModelSerializer):
    logo_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Partner
        fields = '__all__'
    
    def get_logo_url(self, obj):
        return obj.logo.url if obj.logo else None


class ProjectGallerySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = ProjectGallery
        fields = ['id', 'image_url', 'order']
    
    def get_image_url(self, obj):
        return obj.image.url if obj.image else None


class ProjectSerializer(serializers.ModelSerializer):
    gallery = ProjectGallerySerializer(many=True, read_only=True)
    image_url = serializers.SerializerMethodField()
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Project
        fields = '__all__'
    
    def get_image_url(self, obj):
        return obj.image.url if obj.image else None


class TeamMemberSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    
    class Meta:
        model = TeamMember
        fields = '__all__'
    
    def get_photo_url(self, obj):
        return obj.photo.url if obj.photo else None


class DocumentSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Document
        fields = '__all__'
    
    def get_file_url(self, obj):
        return obj.file.url if obj.file else None


class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = '__all__'


class DirectionSerializer(serializers.ModelSerializer):
    icon_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Direction
        fields = '__all__'
    
    def get_icon_url(self, obj):
        return obj.icon.url if obj.icon else None


class NewsSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = News
        fields = '__all__'
    
    def get_image_url(self, obj):
        return obj.image.url if obj.image else None


class FondPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FondPage
        fields = '__all__'


class HistoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryItem
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class HelpSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpSection
        fields = '__all__'


class HelpCardSerializer(serializers.ModelSerializer):
    icon_url = serializers.SerializerMethodField()
    
    class Meta:
        model = HelpCard
        fields = '__all__'
    
    def get_icon_url(self, obj):
        return obj.icon.url if obj.icon else None


class DonationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationRequest
        fields = '__all__'


class PartnerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerRequest
        fields = '__all__'


class VolunteerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerRequest
        fields = '__all__'