from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profiles
from rest_framework import status
from django.http import Http404
from .serializers import ProfileSerializers

# Create your views here.
class ProfileList(APIView):
    def get(self, request):
        profiles = Profiles.objects.all()
        serializer = ProfileSerializers(profiles, many=True)
        return Response(serializer.data)
    

class ProfileDetail(APIView):
    def get_object(self, pk):
        try:
            profile = Profiles.objects.get(pk=pk)
            return profile
        except Profiles.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializers(profile)
        return Response(serializer.data)

    def put(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializers(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(profile)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)