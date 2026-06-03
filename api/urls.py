# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'team', views.TeamMemberViewSet)
router.register(r'documents', views.DocumentViewSet)
router.register(r'home', views.HomePageViewSet)
router.register(r'directions', views.DirectionViewSet)
router.register(r'news', views.NewsViewSet)
router.register(r'fond', views.FondPageViewSet)
router.register(r'history', views.HistoryItemViewSet)
router.register(r'contacts', views.ContactViewSet)
router.register(r'help-section', views.HelpSectionViewSet)
router.register(r'help-cards', views.HelpCardViewSet)
router.register(r'partners', views.PartnerViewSet)
router.register(r'donation-requests', views.DonationRequestViewSet)
router.register(r'partner-requests', views.PartnerRequestViewSet)
router.register(r'volunteer-requests', views.VolunteerRequestViewSet)
router.register(r'hero-slides', views.HeroSlideViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('media/<path:path>', views.serve_media, name='serve_media'),
]