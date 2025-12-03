from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import FileResponse
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Event, Place, RoleCost
from .serializers import EventSerializer, EventPublicSerializer, PlaceSerializer, RoleCostSerializer
from .permissions import IsAdminOrReadOnly
from core.constants import RequestStatus
from .utils import generate_event_report

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
        
    @action(detail=True, methods=['get'], url_path='generate-report', permission_classes=[IsAdminOrReadOnly])
    def generate_report(self, request, pk=None):
        event = self.get_object()
        
        participants_data = []
        
        approved_requests = event.requests.filter(status=RequestStatus.APPROVED).select_related('user')
        
        for req in approved_requests:
            user = req.user
            
            origin_full = ""
            if req.origin_city and req.origin_state:
                origin_full = f"{req.origin_city} / {req.origin_state}"
            elif req.origin_city:
                origin_full = req.origin_city
                
            participants_data.append({
                'name': user.name,
                'email': user.email,
                'cpf': str(user.cpf) if user.cpf else '',
                'birth_date': user.birth_date,
                'role': req.get_role_display(), 
                'phone': req.phone_number,
                'departure_date': req.departure_date,
                'origin': origin_full,
                'return_date': req.return_date,
                'room_type': req.get_room_type_display(),
            })

        report_data = {
            'event_name': event.name,
            'period': f"{event.start_date.strftime('%d/%m/%Y')} to {event.end_date.strftime('%d/%m/%Y')}",
            'location': f"{event.place.name} - {event.place.city}/{event.place.state}",
            'participants': participants_data
        }

        try:
            excel_buffer = generate_event_report(report_data)
        except FileNotFoundError:
            return Response({"error": "Report template not found."}, status=500)
        except Exception as e:
            return Response({"error": str(e)}, status=500)

        filename = f"report_{event.name.replace(' ', '_')}.xlsx"
        response = FileResponse(excel_buffer, as_attachment=True, filename=filename)
        response['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        
        return response
        

        
class PlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [IsAdminOrReadOnly]

class RoleCostViewSet(ModelViewSet):
    queryset = RoleCost.objects.all()
    serializer_class = RoleCostSerializer
    permission_classes = [IsAdminOrReadOnly]

