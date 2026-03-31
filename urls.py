from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "The Gilded Thread Boutique"
admin.site.site_title = "Vintage Atelier"
admin.site.index_title = "Management Console"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]