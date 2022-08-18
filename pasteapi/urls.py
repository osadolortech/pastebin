from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PasteView

router=DefaultRouter()
router.register('paste-bin',PasteView)

urlpatterns = [
    path("",include(router.urls))
]