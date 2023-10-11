from rest_framework import routers

from .viewsets.supplier import SupplierViewSet

router = routers.SimpleRouter()

router.register(r'supplier', SupplierViewSet)
