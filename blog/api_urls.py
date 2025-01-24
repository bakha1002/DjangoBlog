from django.urls import path, include
from .apis import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("viewset", BlogViewSet)

urlpatterns = [
    path("", BlogAPI.as_view()),
    path("generic/", BlogGenericAPI.as_view()),
    path("<int:pk>/", BlogDetailAPI.as_view()),
    path("generic/<int:pk>/", BlogGenericDetailAPI.as_view()),
    path("", include(router.urls)),
    path("hello/", HelloWorldAPI.as_view()),
]
