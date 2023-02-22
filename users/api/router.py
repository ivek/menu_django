from django.urls import path
from rest_framework.routers import DefaultRouter
from users.api.view import UserApiViewSet

router_user = DefaultRouter()

router_user.register(
    prefix='users', basename='users', viewset=UserApiViewSet

)
