from rest_framework import generics, filters
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArtistSerializer, WorkSerializer

class WorkList(generics.ListAPIView):
    serializer_class = WorkSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['artist__name']
    ordering_fields = ['artist__name', 'work_type']

    def get_queryset(self):
        queryset = Work.objects.all()
        artist = self.request.query_params.get('artist', None)
        work_type = self.request.query_params.get('work_type', None)

        if artist is not None:
            queryset = queryset.filter(artist__name=artist)
        if work_type is not None:
            queryset = queryset.filter(work_type=work_type)

        return queryset

class RegisterAPI(generics.CreateAPIView):
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},
                            status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        return Response({
            "username": user.username,
            "id": user.pk
        }, status=status.HTTP_201_CREATED)