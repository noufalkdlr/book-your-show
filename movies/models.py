from django.db import models
from django.utils.text import slugify


class Language(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, db_index=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            count = 1
            while Language.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1
            self.slug = slug
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, db_index=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            count = 1
            while Genre.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1
            self.slug = slug
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, db_index=True)
    photo = models.ImageField(upload_to="directors/", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            count = 1
            while Director.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1
            self.slug = slug
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, db_index=True)
    photo = models.ImageField(upload_to="actors/", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            count = 1
            while Actor.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1
            self.slug = slug
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, db_index=True)
    description = models.TextField(blank=True, default="")
    directors = models.ManyToManyField(Director, related_name="movies")
    cast = models.ManyToManyField(Actor, through="MovieCast", related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies")
    languages = models.ManyToManyField(Language, related_name="movies")
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    poster = models.ImageField(upload_to="movies/poster/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    trailer_url = models.URLField(blank=True, null=True)
    release_date = models.DateField()

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            count = 1
            while Movie.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1
            self.slug = slug
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class MovieCast(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="movie_roles"
    )
    actor = models.ForeignKey(
        Actor, on_delete=models.CASCADE, related_name="actor_roles"
    )
    role_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.actor} as {self.role_name} in {self.movie}"
