from django.contrib import admin
from django.urls import path, include, re_path
from vendors import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Your Project API",
      default_version='v1',
      description="API documentation for Your Project",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/vendors/', include('vendors.urls')),
    path('api/purchase_orders/', include('purchase_orders.urls')),
    path('token/', views.ObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', views.RefreshTokenView.as_view(), name='token_refresh'),
    path('api/performance_metrics/', include('performance_metrics.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]