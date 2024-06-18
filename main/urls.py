from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from api.views import TarefasViewSet
from .views import home

router = DefaultRouter()
router.register(r'tarefas', TarefasViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),

    # djoser auth
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.jwt')),

    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)