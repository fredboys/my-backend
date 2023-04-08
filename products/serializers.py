from rest_framework import serializers
from .models import Product
from save.models import Save
from votes.models import Vote


class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    save_id = serializers.SerializerMethodField()
    save_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    vote_id = serializers.SerializerMethodField()
    vote_count = serializers.ReadOnlyField()

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

    def get_save_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            save = Save.objects.filter(
                owner=user, product=obj
            ).first()
            return save.id if save else None
        return None

    def get_vote_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            vote = Vote.objects.filter(
                owner=user, product=obj
            ).first()
            return vote.id if vote else None
        return None

    class Meta:
        model = Product
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'image', 'is_owner', 'description', 'link', 'price',
            'location', 'profile_id', 'profile_image', 'category_type',
            'save_id', 'save_count', 'comments_count', 'vote_id', 'vote_count'
        ]