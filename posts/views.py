from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from rest_framework import status
from django.http import Http404
from .serializers import PostSerializers
from rest_framework import permissions
# Create your views here.
class PostList(APIView):
    serializer_class = PostSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializers(posts, many=True, context={'request': request})
        return Response(serializer.data)
     
    def post(self, request):
        
        serializer = PostSerializers(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request ,pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status.HTTP_204_NO_CONTENT)