from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r"hello-viewset", views.HelloViewSet,
                basename="hello_viewset")
# if queryset is added there is no need for basename
router.register("profile", views.UserProfileViewSets)
router.register("feed", views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloAPiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),

]
