from django.contrib import admin
from django.urls import path, include

from accounts.urls import translatable_urlpatterns as accounts_urls
from dashboard.urls import translatable_urlpatterns as dashboard_urls


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += accounts_urls
urlpatterns += dashboard_urls