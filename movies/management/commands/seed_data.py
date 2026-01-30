from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from movies.models import Actor, Director, Language, Genre, Movie, MovieCast
from .data import fake_data
from faker import Faker
import random

# Get the correct User model (works even if it's in a different app)
User = get_user_model()


class Command(BaseCommand):
    help = "Seeds the database with dummy data"

    def handle(self, *args, **kwargs):
        fake = Faker()

        for actor in fake_data["actors"]:
            Actor.objects.create(
                name=actor,
            )

        for director in fake_data["directors"]:
            Director.objects.create(
                name=director,
            )

        for language in fake_data["languages"]:
            Language.objects.create(
                name=language,
            )

        for genre in fake_data["genres"]:
            Genre.objects.create(
                name=genre,
            )

        durations = [90, 120, 150, 180, 210, 240]
        all_genre_ids = list(Genre.objects.values_list("id", flat=True))
        all_director_ids = list(Director.objects.values_list("id", flat=True))
        all_language_ids = list(Language.objects.values_list('id',flat=True))
        all_actor_ids = list(Actor.objects.values_list('id',flat=True))
        for movie in fake_data["movies"]:
            year = random.randint(2000, 2026)
            month = random.randint(1, 12)
            day = random.randint(1, 28)
            random_date = f"{year}-{month:02d}-{day:02d}"
            random_genres = random.sample(all_genre_ids, 3)
            random_director = random.choice(all_director_ids)
            random_languages = random.sample(all_language_ids,2)
            random_role_name = random.sample(fake_data["role_name"], 10)
            random_actor = random.sample(all_actor_ids, 10)
            new_movie = Movie.objects.create(
                name=movie,
                description=fake.sentence(30),
                duration=random.choice(durations),
                release_date=random_date,
            )
            new_movie.genres.set(random_genres)
            new_movie.directors.set([random_director])
            new_movie.languages.set(random_languages)
            for actor,role in zip(random_actor,random_role_name):

                MovieCast.objects.create(
                    movie = new_movie,
                    actor_id = actor,
                    role_name = role,
                )

        self.stdout.write(self.style.SUCCESS("Successfully seeded data! 🚀"))
