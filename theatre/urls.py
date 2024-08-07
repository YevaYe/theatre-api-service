from django.urls import path, include
from rest_framework import routers

from theatre.views import GenreViewSet, ActorViewSet, ReservationViewSet, PlayViewSet, TheatreHallViewSet, \
    PerformanceViewSet, TicketViewSet

app_name = "theatre"

router = routers.DefaultRouter()
router.register("reservation", ReservationViewSet)
router.register("actors", ActorViewSet)
router.register("genres", GenreViewSet)
router.register("play", PlayViewSet)
router.register("theatre_hall", TheatreHallViewSet)
router.register("performance", PerformanceViewSet)
router.register("ticket", TicketViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
