from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
]
handler404 = 'events.views.page_not_found'
