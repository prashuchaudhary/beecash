"""BeeCash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls import include, url, static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny


def trigger_error(request):
    division_by_zero = 1 / 0
    print(division_by_zero)


urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(
        r"^api/",
        include(
            [
                url(r"^", include("user_manager.urls")),
            ]
        ),
    )
]

api_info = openapi.Info(
    title="BeeCash API",
    default_version="v1",
    description="BeeCash APIs",
    contact=openapi.Contact(email="prashu.chaudhary7786@gmail.com"),
    license=openapi.License(name="BSD License"),
)

schema_view = get_schema_view(api_info, validators=["flex", "ssv"], public=True, permission_classes=(AllowAny,), )

urlpatterns += [
    url(r"^docs(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    url(r"^docs[/]?$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    url(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
] + static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
