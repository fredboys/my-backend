from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
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
        favourite_count=Count('favourite', distinct=True),
        votes_count=Count('votes', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'favourite__owner__profile',
        'owner__profile',
        'category_type'
    ]
    search_fields = [
        'name',
        'description',
        'category_type'
    ]
    ordering_fields = [
        'favourite_count',
        'comments_count',
        'favourite__created_at',
        'votes_count'
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
        favourite_count=Count('favourite', distinct=True),
        votes_count=Count('votes', distinct=True),
    ).order_by('-created_at')
