from django.db.models import Count
from rest_framework import generics, permissions, filters
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Product
from .serializers import ProductSerializer


class ProductList(generics.ListCreateAPIView):
    """
    List product or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Product.objects.annotate(
        comments_count=Count('comment', distinct=True),
        save_count=Count('save', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'save_count',
        'comments_count',
        'save__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a product and edit or delete it if you own it.
    """
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Product.objects.annotate(
        comments_count=Count('comment', distinct=True),
        save_count=Count('save', distinct=True),
    ).order_by('-created_at')