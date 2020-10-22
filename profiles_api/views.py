from rest_framework.views import APIView
from rest_framework import status
from . import serializers
from . import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework import viewsets
from rest_framework.response import Response


class HelloAPiView(APIView):
    """Test api view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIview features"""
        an_apiview = [
            "Uses http as functions (get post patch ut delete)",
            "Is similar to a traditional django view",
            "Gives you the most control over your application logic"
        ]
        return Response({
            "message": "Hello!",
            "an_api_view": an_apiview
        })

    def post(self, request, format=None):
        """Create hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response({
                "message": message
            })
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """handle updating object"""
        return Response({
            "method": "PUT"
        })

    def patch(self, request, pk=None):
        """handle partial update object"""
        return Response({
            "method": "PATCH"
        })

    def delete(self, request, pk=None):
        """handle delete  object"""
        return Response({"method": "Delete"})


class HelloViewSet(viewsets.ViewSet):
    """"test api views set"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """"Return a hello message"""
        a_viewset = [
            "uses action list (create,read,update,partialupdate) ",
            "automatically maps to url using routerd",
            "Provides more functionality with lesser code"
        ]

        return Response({
            "message": "hello",
            "a_viewset": a_viewset
        })

    def create(self, request):
        """"create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response({
                "message": message,
                # "a_viewset": a_viewset
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """"Handle getting an object by its id"""
        return Response(
            {"http_method": "GET"}
        )

    def update(self, request, pk=None):
        """"Handle getting an object by its id"""
        return Response(
            {"http_method": "PUT"}
        )

    def partial_update(self, request, pk=None):
        """"Handle updating part of an object by its id"""
        return Response({
            "http_method": "PATCH"
        })

    def destroy(self, request, pk=None):
        """"Handle removing an object by its id"""
        return Response({
            "httpmethod": "DELETE"
        })


class UserProfileViewSets(viewsets.ModelViewSet):
    """"handle  creating and updating profiles """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

