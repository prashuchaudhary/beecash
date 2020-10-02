from rest_framework import routers
from user_manager.views.user_view import UserViewSet


router = routers.DefaultRouter()
router.register("user", UserViewSet, basename="user-view")

urlpatterns = router.urls
