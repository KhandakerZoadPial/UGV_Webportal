from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AuthApp.urls')),
    path('AdmissionOffice/', include('AdmissionOffice.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "UGV Administrator"
admin.site.site_title = "UGV Portal"
admin.site.index_title = "Welcome to UGV Administrator Portal"
