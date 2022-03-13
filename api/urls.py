from email.policy import default
from django.db import router
from django.urls import path
from django.conf.urls import include

from rest_framework import routers
from api.views import TaskViewSets, UserViewSet, ManageUserView

router = routers.DefaultRouter
router.register('tasks', TaskViewSets)
router.register('users', UserViewSet)

urlpatterns = [
    path('myself/', ManageUserView.as_view(), name='myself'),
    path('', include(router.urls), name='myself'),
]
