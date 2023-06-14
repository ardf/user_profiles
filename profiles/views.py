# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from django.shortcuts import get_object_or_404

class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get(self, request,pk=None):
        if pk:
            profile = get_object_or_404(Profile, pk=pk)
            serialized_profile = self.serializer_class(profile)
            return Response(data=serialized_profile.data,status=status.HTTP_200_OK)
        
        profiles = Profile.objects.all()
        serialized_profiles = self.serializer_class(profiles,many=True)
        return Response(data=serialized_profiles.data,status=status.HTTP_200_OK)

    def post(self, request,pk=None):
        if pk:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request,pk=None):
        if not pk:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        profile = get_object_or_404(Profile, pk=pk)
        serialized_profile = ProfileSerializer(profile, data=request.data, partial=True)
        if serialized_profile.is_valid():
            serialized_profile.save()
            return Response(data=serialized_profile.data, status=status.HTTP_200_OK)
        return Response(data=serialized_profile.errors, status=status.HTTP_400_BAD_REQUEST)
