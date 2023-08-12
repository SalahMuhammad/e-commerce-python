from django.contrib import admin
from django.urls import path, include
# from rest_framework import routers

from django.conf import settings
from django.conf.urls.static import static

# from items import views
# from django.conf.urls import handler404, handler500


# handler404 = views.handler404

# router = routers.DefaultRouter()
# router.register(r'items', views.ItemsView, 'item')

# router1 = routers.DefaultRouter()
# router1.register(r'item', views.ItemView, 'item')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),
    # path('api/', include(router1.urls)),
    path('', include('items.urls')),
    path('auth/', include('authentication.urls')),
    path('api/', include('api.urls')),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
