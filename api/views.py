from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import FileResponse, Http404
from rest_framework.decorators import api_view
import os
from django.conf import settings
from .models import (
    Project, TeamMember, Document, HomePage,
    Direction, News, FondPage, HistoryItem, Contact,
    HelpSection, HelpCard, Partner,
    DonationRequest, PartnerRequest, VolunteerRequest  # ← ДОБАВЬТЕ ЭТИ МОДЕЛИ
)
from .serializers import (
    ProjectSerializer, TeamMemberSerializer, DocumentSerializer,
    HomePageSerializer, DirectionSerializer, NewsSerializer,
    FondPageSerializer, HistoryItemSerializer, ContactSerializer,
    HelpSectionSerializer, HelpCardSerializer, PartnerSerializer,
    DonationRequestSerializer, PartnerRequestSerializer, VolunteerRequestSerializer
)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]
    lookup_field = "slug"


class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    permission_classes = [AllowAny]  # ← вернули обратно


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [AllowAny]  # ← вернули обратно


class HomePageViewSet(viewsets.ModelViewSet):
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer
    permission_classes = [AllowAny]  # ← вернули обратно

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = self.get_serializer(queryset.first())
            return Response(serializer.data)
        return Response({})


class DirectionViewSet(viewsets.ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer
    permission_classes = [AllowAny]  # ← вернули обратно


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [AllowAny]  # ← вернули обратно


class FondPageViewSet(viewsets.ModelViewSet):
    queryset = FondPage.objects.all()
    serializer_class = FondPageSerializer
    permission_classes = [AllowAny]  # ← вернули обратно

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = self.get_serializer(queryset.first())
            return Response(serializer.data)
        return Response({})


class HistoryItemViewSet(viewsets.ModelViewSet):
    queryset = HistoryItem.objects.all()
    serializer_class = HistoryItemSerializer
    permission_classes = [AllowAny]  # ← вернули обратно


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]  # ← вернули обратно


class HelpSectionViewSet(viewsets.ModelViewSet):
    queryset = HelpSection.objects.all()
    serializer_class = HelpSectionSerializer
    permission_classes = [AllowAny]  # ← вернули обратно

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = self.get_serializer(queryset.first())
            return Response(serializer.data)
        return Response({})


class HelpCardViewSet(viewsets.ModelViewSet):
    queryset = HelpCard.objects.all()
    serializer_class = HelpCardSerializer
    permission_classes = [AllowAny]  # ← вернули обратно

class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = [AllowAny]

class DonationRequestViewSet(viewsets.ModelViewSet):
    queryset = DonationRequest.objects.all()
    serializer_class = DonationRequestSerializer
    permission_classes = [AllowAny]


class PartnerRequestViewSet(viewsets.ModelViewSet):
    queryset = PartnerRequest.objects.all()
    serializer_class = PartnerRequestSerializer
    permission_classes = [AllowAny]


class VolunteerRequestViewSet(viewsets.ModelViewSet):
    queryset = VolunteerRequest.objects.all()
    serializer_class = VolunteerRequestSerializer
    permission_classes = [AllowAny]

@api_view(['GET'])
def serve_media(request, path):
    """Временный эндпоинт для отдачи медиа-файлов."""
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'))
        # Простая проверка на тип файла для правильного Content-Type
        if path.endswith('.png'):
            response['Content-Type'] = 'image/png'
        elif path.endswith('.jpg') or path.endswith('.jpeg'):
            response['Content-Type'] = 'image/jpeg'
        return response
    raise Http404()