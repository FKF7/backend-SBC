from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Event, Place, RoleCost
from .serializers import EventSerializer, EventPublicSerializer, PlaceSerializer, RoleCostSerializer
from .permissions import IsAdminOrReadOnly

# Create your views here.

class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return EventPublicSerializer
        return EventSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [IsAdminOrReadOnly]

class RoleCostViewSet(ModelViewSet):
    queryset = RoleCost.objects.all()
    serializer_class = RoleCostSerializer
    permission_classes = [IsAdminOrReadOnly]

