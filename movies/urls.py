from django.urls import path
from . import views

# Known variable name, meaning we do not have to repeat 'movies_(name of html page)' throughout our code
app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail')
]