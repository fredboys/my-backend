from rest_framework import serializers
from .models import Product
from favourite.models import Favourite
from votes.models import Vote


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    favourite_id = serializers.SerializerMethodField()
    favourite_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    votes_id = serializers.SerializerMethodField()
    votes_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger then 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger then 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger then 4096px'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_favourite_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            favourite = Favourite.objects.filter(
                owner=user, product=obj
            ).first()
            return favourite.id if favourite else None
        return None

    def get_votes_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            votes = Vote.objects.filter(
                owner=user, product=obj
            ).first()
            return votes.id if votes else None
        return None

    class Meta:
        model = Product
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'image', 'is_owner', 'description', 'link', 'price',
            'location', 'profile_id', 'profile_image', 'category_type',
            'favourite_id', 'favourite_count', 'comments_count',
            'votes_id', 'votes_count'
        ]
