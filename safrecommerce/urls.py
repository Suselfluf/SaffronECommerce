from rest_framework import routers
from .api import SaffrViewSet

router = routers.DefaultRouter()
router.register('api/saffron_products', SaffrViewSet, 'safrecommerce')

urlpatterns = router.urls
