from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from rest_framework import status
from django.http import Http404
from .serializers import PostSerializers
from drf_api.permissions import IsOwnerOrReadOnly

# Create your views here.
class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializers(posts, many=True, context={'request': request})
        return Response(serializer.data)
    