"""illusion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

info = openapi.Info(
    title="Illusion API",
    default_version="",
    description="Demonstrate the use of serializers",
    contact=openapi.Contact(
        name="Kalenshi Katebe",
        email="kalenshi@hotmail.com",
        url="https://www.kalenshi.com"
    )
)

schema_view = get_schema_view(info)

urlpatterns = [
    path("api/", include("core.urls")),
    path('', schema_view.with_ui("swagger"), name="swagger"),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),
