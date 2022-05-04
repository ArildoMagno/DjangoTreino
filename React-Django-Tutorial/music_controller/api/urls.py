from django.urls import path
from .views import RoomView
from .views import CreateRoomView
from .views import GetRoom
from .views import UserInRoom

urlpatterns = [
    path('room', RoomView.as_view()),
    path('create-room', CreateRoomView.as_view()),
    path('get-room', GetRoom.as_view()),
    path('user-in-room', UserInRoom.as_view()),
]
