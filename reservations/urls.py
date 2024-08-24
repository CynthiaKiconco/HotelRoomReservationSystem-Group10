from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, RoomTypeViewSet, RoomViewSet, ReservationViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'roomtypes', RoomTypeViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
