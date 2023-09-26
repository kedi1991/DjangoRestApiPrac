from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Comment
from rest_framework import status
from django.http import Http404
from .serializers import CommentSerializers
from rest_framework import permissions
# Create your views here.
class CommentList(APIView):
    serializer_class = CommentSerializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializers(comments, many=True, context={'request': request})
        return Response(serializer.data)