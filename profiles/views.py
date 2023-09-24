from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profiles
from .serializers import ProfileSerializers

# Create your views here.
class ProfileList(APIView):
    def get(self, request):
        profiles = Profiles.objects.all()
        serializer = ProfileSerializers(profiles, many=True)
        return Response(serializer.data)
    