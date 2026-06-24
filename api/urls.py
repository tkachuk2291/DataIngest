from django.urls import re_path, path
from api import views
from DataAggregate.views import AggregateView

urlpatterns = [
    re_path(r"^file/(?P<filename>[^/]+)$", views.IngestView.as_view(), name="file"),
    path('aggregate/', AggregateView.as_view(), name='aggregate'),
]