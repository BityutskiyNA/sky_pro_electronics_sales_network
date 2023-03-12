from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import CounterpartyView

router = routers.SimpleRouter()
router.register('counterparty',CounterpartyView)


urlpatterns = [

]


urlpatterns+= router.urls