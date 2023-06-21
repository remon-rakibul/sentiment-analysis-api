from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
]

handler404 = 'utils.views.error_404'
handler500 = 'utils.views.error_500'