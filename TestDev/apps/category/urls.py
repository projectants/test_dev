from rest_framework import routers

from .viewsets.category import CategoryViewSet

router = routers.SimpleRouter()

router.register(r'category', CategoryViewSet)
