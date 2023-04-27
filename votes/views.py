from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Vote
from .serializers import VoteSerializer


class VoteList(generics.ListCreateAPIView):
    """
    lists all votes
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VoteDetail(generics.RetrieveDestroyAPIView):
    """
    Allows to delete votes
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()
