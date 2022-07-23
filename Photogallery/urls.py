from django.urls import path
from .views import gallery_view

app_name = 'Photogallery'
urlpatterns = [
    path('', gallery_view, name='photos')
]