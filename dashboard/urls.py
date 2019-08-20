from django.conf.urls import url
from django.urls import include, path
from . import views
from .views import TourDelete, TourUpdate, TourCreate, PackageUpdate
from django.contrib.auth.decorators import login_required
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/tours', views.ToursViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^packages/$', login_required(views.packages), name='tour_packages'),
    url(r'^packages/(?P<pk>[\w]+)/update/$', login_required(PackageUpdate.as_view()), {}, name='pkg_update'),

    url(r'^tour/create/$', login_required(TourCreate.as_view()), name='tour_create'),
    url(r'^tour/(?P<pk>\d+)/edit/$', login_required(TourUpdate.as_view()), {}, name='tour_edit'),
    url(r'^tour/(?P<pk>[\w]+)/delete/$', login_required(TourDelete.as_view()), {}, name='tour_delete'),

    path('', include(router.urls)),
]


