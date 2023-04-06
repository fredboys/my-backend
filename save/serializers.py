from django.db import IntegrityError
from rest_framework import serializers
from .models import Save


class SaveSerializer(serializers.ModelSerializer):
    """
    Serializer for the Save model
    The create method handles the unique constraint on 'owner' and 'product'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Save
        fields = ['id', 'owner', 'created_at', 'product']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
