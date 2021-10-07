from django.db import models


class Genre(models.Model):
    genre_choices = (
        ('action', 'Action'),
        ('adventure', 'Adventure'),
        ('animation', 'Animation'),
        ('biography', 'Biography'),
        ('comedy', 'Comedy'),
        ('crime', 'Crime'),
        ('documentary', 'Documentary'),
        ('drama', 'Drama'),
        ('family', 'Family'),
        ('fantasy', 'Fantasy'),
        ('history', 'History'),
        ('horror', 'Horror'),
        ('music', 'Music'),
        ('mystery', 'Mystery'),
        ('romance', 'Romance'),
        ('sci-fi', 'Sci-Fi'),
        ('short', 'Short'),
        ('thriller', 'Thriller'),
        ('war', 'War'),
        ('western', 'Western'),
    )

    genre = models.CharField(choices=genre_choices, max_length=30,
                             help_text='Please a movie genre')

    def __str__(self):
        return self.genre


class Language(models.Model):
    name = models.CharField(max_length=30, help_text='Please add a language')

    # short_name = models.CharField(max_length=10, help_text='Select a short name')

    def __str__(self):
        return self.name


class Person(models.Model):

    first_name = models.CharField(max_length=100,
                                  help_text='Enter first name of the person')

    last_name = models.CharField(max_length=100,
                                 help_text='Enter last name of the person')

    date_of_birth = models.DateField(null=True, blank=True)

    date_of_death = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.first_name + self.last_name


class Movie(models.Model):

    # title of the movie 1. Should be unique
    original_title = models.CharField(max_length=2000, unique=True)

    release_date = models.DateField('Date released')

    # tag line
    tagline = models.CharField(max_length=100)

    # description
    overview = models.TextField(
        max_length=1000,
        help_text='Please enter a brief description for this movie')

    # poster url
    poster_path = models.CharField(max_length=100)

    # manytomany field => because a movie can cover multiple genre & a genre can have many movies
    genres = models.ManyToManyField(Genre)

    # restricting language to only 1 language
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, default='en', null=True)

    # duration of the movie
    length = models.TimeField()

    cast = models.ManyToManyField(Person, related_name='cast')

    director = models.ForeignKey(Person, on_delete=models.SET_NULL, related_name='directors', null=True)

    # production company

    def __str__(self):
        return self.original_title
