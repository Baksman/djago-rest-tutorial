from rest_framework import serializers
from . import models


class HelloSerializer(serializers.Serializer):
    """Serializes A name field for testing out api view"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """"Serializes a user profileobject"""
    class Meta:
        model = models.UserProfile
        fields = ("id", "email", "name", "password")
        extra_kwargs = {
            "password": {
                "write_only": True,
                "style": {
                    "input_type": "password"
                }
            }
        }

        def create(self, validated_data):
            """create and return a new user"""
            user = models.UserProfile.objects.create_user(
                email=validated_data["email"],
                password=validated_data["password"],
                name=validated_data["name"]
            )
            return user


class ProfileFeedItemSerilizer(serializers.ModelSerializer):
    """serializes profile feed items"""
    class Meta:
        model = models.ProfileFeedItem
        fields = ("id", "user_profile", "status_text", "created_on")
        extra_kwargs = {
            "user_profile": {
                "read_only": True
            }
        }
