from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
]

handler404 = 'products.views.page_not_found'
