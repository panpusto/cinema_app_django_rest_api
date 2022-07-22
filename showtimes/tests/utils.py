from random import sample, randint, choice

import pytz
from faker import Faker

from moviebase.settings import TIME_ZONE
from movielist.models import Movie
from showtimes.models import Cinema, Screening

faker = Faker("pl_PL")
TZ = pytz.timezone(TIME_ZONE)


def random_movies():
    """Return 5 random Movies from database."""
    movies = list(Movie.objects.all())
    return sample(movies, 5)


def add_screenings(cinema):
    """Add 5 screenings for given cinema."""
    movies = random_movies()
    for movie in movies:
        Screening.objects.create(movie=movie, cinema=cinema, date=faker.date_time(tzinfo=TZ))


def fake_cinema_data():
    """Generate a dict of cinema data

    The format is compatible with serializers ('Cinema' relations
    represented by names).
    """
    return {
        'name': faker.name(),
        'city': faker.city(),
    }


def create_fake_cinema():
    """Create fake cinema with some screenings"""
    cinema = Cinema.objects.create(**fake_cinema_data())
    add_screenings(cinema)
