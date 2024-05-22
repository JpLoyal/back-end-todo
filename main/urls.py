from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from api.views import TarefasViewSet
from .views import home

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'tarefas', TarefasViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),

    # Rota para obter um token de acesso
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Rota para atualizar um token de acesso (renovar token)
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
