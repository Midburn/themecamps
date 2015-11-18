from django.conf.urls import url, include
from rest_framework import routers
from themecampsapp import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'camps', views.CampViewSet)
router.register(r'camps_locations', views.CampLocationViewSet)
router.register(r'camps_members', views.CampMemberViewSet)
router.register(r'camps_safety', views.CampSafetyViewSet)
router.register(r'workshops', views.WorkshopViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]