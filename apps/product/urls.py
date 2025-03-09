from rest_framework.routers import DefaultRouter
from apps.product.views import ProductMixins,CategoryViewSet

router = DefaultRouter()
router.register(r"product", ProductMixins, basename="product")
router.register(r"category", CategoryViewSet)

urlpatterns = router.urls