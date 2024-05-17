from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from api.views import TarefasViewSet

router = DefaultRouter()
router.register(r'tarefas', TarefasViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
