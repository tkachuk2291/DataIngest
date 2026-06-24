from rest_framework.routers import DefaultRouter
from User import views

router = DefaultRouter()
router.register(r"users", views.UserViewSet, basename="user")