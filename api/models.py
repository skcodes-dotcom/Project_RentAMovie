from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie

# queryset = Movie.objects.all() : Returns a query. We are setting this query to get a list of our movies.
#  resource_name = 'movies' : This determines what our Endpoint will look like.
# excludes = ['date_created']  Do not show the created date of the movies


class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
        excludes = ['date_created']
