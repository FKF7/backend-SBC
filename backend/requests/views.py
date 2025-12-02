from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Request
from .serializers import RequestSerializer
from .permissions import IsAdminOrOwner
from core.constants import RequestStatus

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.select_related("user", "event").all()
    serializer_class = RequestSerializer
    permission_classes = [IsAuthenticated, IsAdminOrOwner]

    def get_queryset(self):
        qs = super().get_queryset()

        event_uuid = self.request.query_params.get("event")
        if event_uuid:
            qs = qs.filter(event__uuid=event_uuid)

        user = self.request.user
        if user and not user.is_staff:
            qs = qs.filter(user=user)

        return qs
    
    @action(detail=False, methods=["get"], url_path="by-user-event")
    def get_by_user_and_event(self, request):
        user = request.user
        event_uuid = request.query_params.get("event")

        if not event_uuid:
            return Response({"detail": "Missing event param."}, status=400)

        try:
            req = Request.objects.get(user=user, event__uuid=event_uuid)
            serializer = self.get_serializer(req)
            return Response(serializer.data)
        except Request.DoesNotExist:
            return Response(None, status=200)

    @action(detail=True, methods=["patch"], permission_classes=[IsAdminUser])
    def approve(self, request, pk=None):
        req = self.get_object()

        if req.status == RequestStatus.APPROVED:
            return Response(
                {"detail": "Essa solicitação já está aprovada."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        req.status = RequestStatus.APPROVED
        req.save()
        return Response({"detail": "Solicitação aprovada."})


    @action(detail=True, methods=["patch"], permission_classes=[IsAdminUser])
    def reject(self, request, pk=None):
        req = self.get_object()

        if req.status == RequestStatus.REJECTED:
            return Response(
                {"detail": "Essa solicitação já está rejeitada."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        req.status = RequestStatus.REJECTED
        req.save()
        return Response({"detail": "Solicitação rejeitada."})
