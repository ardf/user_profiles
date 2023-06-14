"""
    views.py - Profile API Views

    This module contains the views for managing user profiles through the API.
    It provides endpoints to create, retrieve, update, and delete user profiles.

    Classes:
    - ProfileAPIView: API view class for managing user profiles.

    Permissions:
    - IsAuthenticated: Only authenticated users can access the endpoints.

    Serializers:
    - ProfileSerializer: Serializer class for the Profile model.

    Models:
    - Profile: Model representing user profiles.

"""
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from django.shortcuts import get_object_or_404

class ProfileAPIView(APIView):
    """
    ProfileAPIView

    API view class for managing user profiles.

    Endpoints:
    - GET: Retrieve a list of all profiles or a specific profile.
    - POST: Create a new profile.
    - PATCH: Update an existing profile.

    Permission Classes:
    - IsAuthenticated: Only authenticated users can access the endpoints.

    Serializer Class:
    - ProfileSerializer: Serializer class for the Profile model.

    """
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer

    def get(self, request,pk=None):
        """
        Retrieve a list of all profiles or a specific profile.

        Args:
        - request: The request object.
        - pk: Optional profile ID to retrieve a specific profile.

        Returns:
        - Response with serialized profile data or list of serialized profiles.

        """
        if pk:
            profile = get_object_or_404(Profile, pk=pk)
            serialized_profile = self.serializer_class(profile)
            return Response(data=serialized_profile.data,status=status.HTTP_200_OK)
        
        profiles = Profile.objects.all()
        serialized_profiles = self.serializer_class(profiles,many=True)
        return Response(data=serialized_profiles.data,status=status.HTTP_200_OK)

    def post(self, request,pk=None):
        """
        Create a new profile.

        Args:
        - request: The request object.
        - pk: Not used in this method.

        Returns:
        - Response with serialized profile data if successful, otherwise error response.

        """
        if pk:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request,pk=None):
        """
        Update an existing profile.

        Args:
        - request: The request object.
        - pk: The ID of the profile to be updated.

        Returns:
        - Response with serialized profile data if successful, otherwise error response.

        """
        if not pk:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        profile = get_object_or_404(Profile, pk=pk)
        serialized_profile = ProfileSerializer(profile, data=request.data, partial=True)
        if serialized_profile.is_valid():
            serialized_profile.save()
            return Response(data=serialized_profile.data, status=status.HTTP_200_OK)
        return Response(data=serialized_profile.errors, status=status.HTTP_400_BAD_REQUEST)
