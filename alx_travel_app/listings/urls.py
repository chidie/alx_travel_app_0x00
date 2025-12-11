from rest_framework.routers import DefaultRouter
from .views import ListingViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r"listings", ListingViewSet, basename='listing')

urlpatterns = [
    path('', include(router.urls)),
    
]