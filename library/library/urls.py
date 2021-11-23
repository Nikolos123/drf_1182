"""library URL Configuration

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
from django.urls import path,include
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter,SimpleRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
import users
from authors.views import AuthorModelViewSet,BiographyModelViewSet,BookModelViewSet
from users.views import UserListAPIView

schema_view = get_schema_view(
    openapi.Info(
        title='Library',
        default_version='v2',
        description='Documentation for our projects',
        contact=openapi.Contact(email='django@django.ru'),
        license=openapi.License(name='MIT License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)



router = DefaultRouter()
router.register('authors',AuthorModelViewSet)
router.register('book',BookModelViewSet)
router.register('biography',BiographyModelViewSet)

#http://v1.example.com

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api-token-auth/',obtain_auth_token),
    # path('swagger/',schema_view.with_ui('swagger')),
    path('swagger<str:format>/',schema_view.without_ui()),
    path('redoc/',schema_view.with_ui('redoc')),
    # path('api/<str:version>/users/', UserListAPIView.as_view())
    # path('api/users/v1', include('users.urls',namespace='v1')),
    # path('api/users/v2', include('users.urls',namespace='v2'))

]
