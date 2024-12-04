from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = [path("__debug__/", include(debug_toolbar_urls()))] + urlpatterns
