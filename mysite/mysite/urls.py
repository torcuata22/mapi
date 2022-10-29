"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from movies.views import MovieViewSet, ActionViewSet, FantasyViewSet, SciFiViewSet, CrimeViewSet

router = routers.SimpleRouter() #variable = routers we imported.method, changed method from DefaultRouter to SImpleRouter
router.register('movies', MovieViewSet) #registers the view
router.register('action', ActionViewSet)
router.register('fantasy', FantasyViewSet)
router.register('scifi', SciFiViewSet)
router.register('crime', CrimeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
