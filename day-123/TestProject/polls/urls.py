from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('query', views.query, name='query'),
    path('update', views.update, name='update'),
    path('del', views.delete, name='del'),
]
