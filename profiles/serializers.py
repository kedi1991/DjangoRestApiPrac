from rest_framework import serializers
from .models import Profiles

class ProfileSerializers(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profiles
        fields = [
            'id', 'owner', 'created_at', 'updated_At', 'name', 'content', 'image'
        ]