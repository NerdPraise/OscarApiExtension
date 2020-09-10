# Third party import
from rest_framework import routers

# Local import
from . import views

router = routers.DefaultRouter()
router.register(r"user", views.UserViewAPI, basename="user_api")


urlpatterns = router.urls
