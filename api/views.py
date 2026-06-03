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
    DonationRequest, PartnerRequest, VolunteerRequest
)
from .serializers import (
    ProjectSerializer, TeamMemberSerializer, DocumentSerializer,
    HomePageSerializer, DirectionSerializer, NewsSerializer,
    FondPageSerializer, HistoryItemSerializer, ContactSerializer,
    HelpSectionSerializer, HelpCardSerializer, PartnerSerializer,
    DonationRequestSerializer, PartnerRequestSerializer, VolunteerRequestSerializer
)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()  # ← ЭТО ДОЛЖНО БЫТЬ
    serializer_class = ProjectSerializer  # ← ЭТО ДОЛЖНО БЫТЬ
    permission_classes = [AllowAny]
    lookup_field = "slug"


class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()  # ← ЭТО ДОЛЖНО БЫТЬ
    serializer_class = TeamMemberSerializer  # ← ЭТО ДОЛЖНО БЫТЬ
    permission_classes = [AllowAny]


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()  # ← ЭТО ДОЛЖНО БЫТЬ
    serializer_class = DocumentSerializer  # ← ЭТО ДОЛЖНО БЫТЬ
    permission_classes = [AllowAny]


class HomePageViewSet(viewsets.ModelViewSet):
    queryset = HomePage.objects.all()  # ← ЭТО ДОЛЖНО БЫТЬ
    serializer_class = HomePageSerializer  # ← ЭТО ДОЛЖНО БЫТЬ
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = self.get_serializer(queryset.first())
            return Response(serializer.data)
        return Response({})


class DirectionViewSet(viewsets.ModelViewSet):
    queryset = Direction.objects.all()  # ← ЭТО ДОЛЖНО БЫТЬ
    serializer_class = DirectionSerializer  # ← ЭТО ДОЛЖНО БЫТЬ
    permission_classes = [AllowAny]


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()  # ← ЭТО ДОЛЖНО БЫТЬ
    serializer_class = NewsSerializer  # ← ЭТО ДОЛЖНО БЫТЬ
    permission_classes = [AllowAny]


class FondPageViewSet(viewsets.ModelViewSet):
    queryset = FondPage.objects.all()  # ← ЭТО ДОЛЖНО БЫТЬ
    serializer_class = FondPageSerializer  # ← ЭТО ДОЛЖНО БЫТЬ
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = self.get_serializer(queryset.first())
            return Response(serializer.data)
        return Response({})


class HistoryItemViewSet(viewsets.ModelViewSet):
    queryset = HistoryItem.objects.all()  # ← ЭТО ДОЛЖНО БЫТЬ
    serializer_class = HistoryItemSerializer  # ← ЭТО ДОЛЖНО БЫТЬ
    permission_classes = [AllowAny]


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()  # ← ЭТО ДОЛЖНО БЫТЬ
    serializer_class = ContactSerializer  # ← ЭТО ДОЛЖНО БЫТЬ
    permission_classes = [AllowAny]


class HelpSectionViewSet(viewsets.ModelViewSet):
    queryset = HelpSection.objects.all()  # ← ЭТО ДОЛЖНО БЫТЬ
    serializer_class = HelpSectionSerializer  # ← ЭТО ДОЛЖНО БЫТЬ
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = self.get_serializer(queryset.first())
            return Response(serializer.data)
        return Response({})


class HelpCardViewSet(viewsets.ModelViewSet):
    queryset = HelpCard.objects.all()  # ← ЭТО ДОЛЖНО БЫТЬ
    serializer_class = HelpCardSerializer  # ← ЭТО ДОЛЖНО БЫТЬ
    permission_classes = [AllowAny]


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()  # ← ЭТО ДОЛЖНО БЫТЬ
    serializer_class = PartnerSerializer  # ← ЭТО ДОЛЖНО БЫТЬ
    permission_classes = [AllowAny]


class DonationRequestViewSet(viewsets.ModelViewSet):
    queryset = DonationRequest.objects.all()  # ← ЭТО ДОЛЖНО БЫТЬ
    serializer_class = DonationRequestSerializer  # ← ЭТО ДОЛЖНО БЫТЬ
    permission_classes = [AllowAny]


class PartnerRequestViewSet(viewsets.ModelViewSet):
    queryset = PartnerRequest.objects.all()  # ← ЭТО ДОЛЖНО БЫТЬ
    serializer_class = PartnerRequestSerializer  # ← ЭТО ДОЛЖНО БЫТЬ
    permission_classes = [AllowAny]


class VolunteerRequestViewSet(viewsets.ModelViewSet):
    queryset = VolunteerRequest.objects.all()  # ← ЭТО ДОЛЖНО БЫТЬ
    serializer_class = VolunteerRequestSerializer  # ← ЭТО ДОЛЖНО БЫТЬ
    permission_classes = [AllowAny]


@api_view(['GET'])
def serve_media(request, path):
    """Временный эндпоинт для отдачи медиа-файлов."""
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'))
        if path.endswith('.png'):
            response['Content-Type'] = 'image/png'
        elif path.endswith('.jpg') or path.endswith('.jpeg'):
            response['Content-Type'] = 'image/jpeg'
        return response
    raise Http404()