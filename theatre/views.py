from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from theatre.models import Reservation, Actor, Genre, Play, TheatreHall, Performance, Ticket
from theatre.permissions import IsAdminOrIfAuthenticatedReadOnly
from theatre.serializers import (
    ReservationSerializer,
    ActorSerializer,
    GenreSerializer,
    PlaySerializer,
    TheatreHallSerializer,
    PerformanceSerializer,
    TicketSerializer
)


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]


class PlayViewSet(viewsets.ModelViewSet):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]


class TheatreHallViewSet(viewsets.ModelViewSet):
    queryset = TheatreHall.objects.all()
    serializer_class = TheatreHallSerializer
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAdminOrIfAuthenticatedReadOnly]
