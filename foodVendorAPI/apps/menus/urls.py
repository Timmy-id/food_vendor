from django.urls import path, include
from rest_framework import routers
from .views import MenuViewSet


router = routers.DefaultRouter()
router.register(r'', MenuViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
