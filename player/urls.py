from django.urls import path
from . import views
urlpatterns = [
    path("player/", views.PlayerListView.as_view(), name='player_list'),
    path('add/', views.PlayerAdView.as_view(), name='add')
]