from django.urls import path
from .views import EmployeeListCreateAPIView, EmployeeRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', EmployeeListCreateAPIView.as_view()),
    path('<int:id>/', EmployeeRetrieveUpdateDestroyAPIView.as_view())
]