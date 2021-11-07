from django.urls import path

from . import views
urlpatterns = [

    path('', views.home, name='home'),
    path('subtract',views.subtract, name='subtract')
]
