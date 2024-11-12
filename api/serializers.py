from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile, Post, Comment, Vote, Tag
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.middleware.csrf import get_token
from django.contrib.auth.hashers import check_password
from django.db import models


class CustomTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_id'] = user.id  # Add user ID to the token
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_id'] = self.user.id  # Add user ID to the response

        request = self.context.get('request')
        if request:
            data['csrfToken'] = get_token(request)
        return datadata


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance


class VoteSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id', read_only=True)

    class Meta:
        model = Vote
        fields = ['user_id', 'value']


class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    author_id = serializers.IntegerField(source='author.id', read_only=True)
    upvotes = serializers.IntegerField(read_only=True)
    downvotes = serializers.IntegerField(read_only=True)
    total_votes = serializers.IntegerField(read_only=True)
    votes = VoteSerializer(many=True, read_only=True)
    post_title = serializers.CharField(source='post.title', read_only=True)
    post_id = serializers.IntegerField(source='post.id', read_only=True)

    class Meta:
        model = Comment
        fields = [
            'id',
            'post_id',
            'post_title',
            'author_id',
            'author_username',
            'content',
            'created_at',
            'updated_at',
            'upvotes',
            'downvotes',
            'total_votes',
            'votes',
        ]
        read_only_fields = [
            'post_id',
            'created_at',
            'updated_at',
            'upvotes',
            'downvotes',
            'total_votes',
        ]
