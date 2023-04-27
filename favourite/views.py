from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Favourite
from .serializers import FavouriteSerializer


class FavouriteList(generics.ListCreateAPIView):
    """
    List all the favourites
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FavouriteSerializer
    queryset = Favourite.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FavouriteDetail(generics.RetrieveDestroyAPIView):
    """
    Allows delete of a favourite
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FavouriteSerializer
    queryset = Favourite.objects.all()
