from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
    IsAuthenticatedOrReadOnly,
)
from django.db.models import Prefetch, Q
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from django.middleware.csrf import get_token
from django.http import Http404, JsonResponse
from .serializers import (
    UserSerializer,
    PostSerializer,
    CommentSerializer,
    CustomTokenSerializer,
    UserProfileSerializer,
    ChangePasswordSerializer,
)
from .models import Post, Comment, Vote, UserProfile
from rest_framework.exceptions import NotFound


def csrf_token_view(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})


class CustomTokenView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()

        UserProfile.objects.create(user=user)


class EditUserView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_object(self):
        # Ensure the user is only updating their own profile
        return self.request.user

    def perform_update(self, serializer):
        user = serializer.save()

        user_profile, created = UserProfile.objects.get_or_create(user=user)

        # UserProfile update
        user_profile.bio = self.request.data.get('bio', user_profile.bio)
        user_profile.profile_picture = self.request.data.get(
            'profile_picture', user_profile.profile_picture
        )
        user_profile.save()

        return user  

