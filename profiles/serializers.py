from rest_framework import serializers
from .models import Profiles

class ProfileSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request=self.context['request']
        return request.user == obj.owner
    class Meta:
        model = Profiles
        fields = [
            'id', 'owner', 'created_at', 'updated_At', 'name', 'content', 'image', 'is_owner'
        ]