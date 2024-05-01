"""
URL configuration for vendorapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from vendors import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/vendors/', include('vendors.urls')),
    path('api/purchase_orders/', include('purchase_orders.urls')),
    path('token/', views.ObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', views.RefreshTokenView.as_view(), name='token_refresh'),
    # path('api/performance_metrics/', include('performance_metrics.urls')),
]

