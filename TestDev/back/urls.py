from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from apps.category.urls import router as category_router
from apps.product.urls import router as product_router
from apps.supplier.urls import router as supplier_router

router = routers.DefaultRouter()

router.registry.extend(product_router.registry)
router.registry.extend(supplier_router.registry)
router.registry.extend(category_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include((router.urls, "root"))),
    path('auth/', include('rest_framework.urls')),
]
