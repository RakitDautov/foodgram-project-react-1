from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('users', CustomUserViewSet)

urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls)),
    #path('', include('djoser.urls'))
]
