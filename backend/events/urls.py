from rest_framework.routers import DefaultRouter
from .views import EventViewSet, PlaceViewSet, RoleCostViewSet

router = DefaultRouter()
router.register("events", EventViewSet, basename="events")
router.register("places", PlaceViewSet, basename="places")
router.register("rolecosts", RoleCostViewSet, basename="rolecosts")

urlpatterns = router.urls
