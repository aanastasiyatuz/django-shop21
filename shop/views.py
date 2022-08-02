from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product, Category, Comment, Like
from .serializers import ProductSerializer, CategorySerializer, CommentSerializer
from .permissions import IsAuthor

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CategoryViewSet(mixins.CreateModelMixin, 
                    mixins.DestroyModelMixin, 
                    mixins.ListModelMixin, 
                    GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CommentViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

@api_view(["GET"])
def toggle_like(request, p_id):
    user = request.user
    product = get_object_or_404(Product, id=p_id)

    if Like.objects.filter(user=user, product=product).exists():
        Like.objects.filter(user=user, product=product).delete()
    else:
        Like.objects.create(user=user, product=product)
    return Response("Like toggled", 200)
