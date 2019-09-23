# esto es una views dentro de walkers, no se por que, pero importo tmb las views dentro del proyecto y fuera de walkers
from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
]