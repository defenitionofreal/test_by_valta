from .views import CatalogViewSet

from rest_framework import routers

app_name = 'catalog'

router = routers.DefaultRouter()
router.register('catalog', CatalogViewSet, basename='catalog')

urlpatterns = []
urlpatterns += router.urls
