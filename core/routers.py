from rest_framework import routers

from core.user.viewssets import UserViewSet

router = routers.SimpleRouter()

# ##################################################################### #
# ################### USER                       ###################### #
# ##################################################################### #

router.register(r"user", UserViewSet, basename="user")

urlpatterns = [
    *router.urls
]
