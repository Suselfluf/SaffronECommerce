from rest_framework import routers
from .api import SaffrViewSet

router = routers.DefaultRouter()
router.register('api/todo', SaffrViewSet, 'safrecommerce')

urlpatterns = router.urls
