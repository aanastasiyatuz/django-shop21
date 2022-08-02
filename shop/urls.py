from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, CategoryViewSet, CommentViewSet, toggle_like

router = DefaultRouter()
router.register("products", ProductViewSet)
router.register("categories", CategoryViewSet)
router.register("comments", CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('toggle_like/<int:p_id>/', toggle_like),
]