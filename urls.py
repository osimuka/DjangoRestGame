from django.urls import re_path
from rest_framework import routers
from . import views

app_name = 'game_api'

router = routers.SimpleRouter()

urlpatterns = [
    re_path(r'^api/v1/game-data/$', views.NewGameUser.as_view()),
    re_path(
        r'^api/v1/game-data/(?P<user_id>[-\w]+)/$',
        views.GameUser.as_view()),
]
