"""urls.py"""

from django.urls import path, include

from rest_framework.routers import DefaultRouter

from journal.views import TagViewSet, PostViewSet


router = DefaultRouter()

router.register(r'tags', TagViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [path('', include(router.urls))]
