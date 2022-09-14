from turtle import title
from blog.models import Post
from .serializers import PostSerializer

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, DjangoModelPermissions, IsAuthenticated
from rest_framework import filters
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from django.shortcuts import get_object_or_404
# import { useNavigate } from 'react-router-dom';

# """ permissions for user to post and get and put data """
class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

"""
video-7

display POSTs
"""
class PostList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug = item)

class PostListDetailfilter(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter] # drf packeges for search filters
    search_fields = ['^slug'] # drf packeges for search filters


# Post Admin
class AdminPostList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)


class CreatePost(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(author=user)

# class CreatePost(APIView):
#     permission_classes = [IsAuthenticated]
#     parser_classes = [MultiPartParser, FormParser]

#     def post(self, request, format=None):
#         print(request.data)
#         serializer = PostSerializer(data = request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminPostDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class EditPost(generics.RetrieveUpdateAPIView):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_update(self, serializer):
        user = self.request.user
        serializer.save(author=user)

class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

















# """
# video - 6 start
# """
# """ generic class base views (Video-6)"""
# class PostList(generics.ListAPIView):
#     # queryset = Post.postobjects.all()
#     permission_classes = [DjangoModelPermissions]
#     serializer_class = PostSerializer

#     # show all posts that user made usefull when using dashboard
#     def get_queryset(self):
#         user = self.request.user
#         return Post.objects.filter(author=user)

# class PostDetail(generics.RetrieveAPIView):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Post, slug=item)
#     # def get_queryset(self):
#     #     slug = self.request.query_params.get('slug', None)
#     #     return Post.objects.filter(slug=slug)

# class PostListDetailfilter(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     filter_backends = [filters.SearchFilter] # drf packeges for search filters
#     search_fields = ['^slug'] # drf packeges for search filters

    # '^' Starts-with search.
    # '=' Exact matches.
    # '@' Full-text search. (Currently only supported Django's PostgreSQL backend.)
    # '$' Regex search.

    # PostDetail method of queryset to get single object using pk
    # def get_queryset(self):
    #     """
    #     Example #2 Part 1
    #     Filtering against the URL (ID)
    #     Get post based on title /string
    #     """
    #     slug = self.kwargs['pk']
    #     print(slug)
    #     return Post.objects.filter(id=slug)

# get single data using slug
# class PostDetail(generics.RetrieveAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Post, slug=item)

# class PostList(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
    
#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Post, slug=item)
        
#     # define a custom query set
#     def get_queryset(self):
#         return Post.objects.all()
# """
# video - 6 start
# """


# """ ViewSet for list and retrieve """
# class PostList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.postobjects.all()

#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response (serializer_class.data)

#     def retrieve(self, request, pk = None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)


# class PostList(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.postobjects.all()
#     serializer_class = PostSerializer


# class PostDetail(viewsets.ModelViewSet, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


