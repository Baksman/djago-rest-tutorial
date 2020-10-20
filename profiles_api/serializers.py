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
