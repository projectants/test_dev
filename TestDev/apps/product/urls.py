from rest_framework import routers

from .viewsets.product import ProductViewSet

router = routers.SimpleRouter()

router.register(r'product', ProductViewSet)
