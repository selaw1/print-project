from django.urls import path
from django.conf.urls.i18n import i18n_patterns

from dashboard import views



translatable_urlpatterns = i18n_patterns(
    path('dashboard/home', views.DashboardView.as_view(), name="dash-home")
)
