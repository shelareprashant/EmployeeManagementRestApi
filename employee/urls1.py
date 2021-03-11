from django.urls import path, include
from rest_framework import routers

from .views import EmployeeCRUDCBV

router = routers.DefaultRouter()
router.register('emp-data', EmployeeCRUDCBV, basename='emp-data')


urlpatterns = [
    path('', include(router.urls))
]