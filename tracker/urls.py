from django.urls import path
from tracker.views import UnitListCreateView, VisitListCreateView

urlpatterns = [
    path('units/', UnitListCreateView.as_view(), name='unit-list-create'),
    path('visits/', VisitListCreateView.as_view(), name='visit-list-create'),
]
