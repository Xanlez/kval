from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employees.urls')),
]
handler404 = 'employees.views.page_not_found'
