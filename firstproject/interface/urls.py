from django.urls import path

from . import views

app_name = 'interface'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('file', views.FileView.as_view(), name='file'),
    path('teste', views.TesteView.as_view(), name='teste'),
    path('print_function', views.print_function, name='print_function'),
    path('upload/', views.upload, name='upload'),
]