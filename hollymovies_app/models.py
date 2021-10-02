from django.db import models


class Genre(models.Model):
    HORROR = 'HR'
    COMEDY = 'CM'
    GENRE_NAME_CHOICES = [
        (HORROR, 'Horror'),
        (COMEDY, 'Comedy'),
    ]
    name = models.CharField(choices=GENRE_NAME_CHOICES, max_length=2)

    def is_genre_horror(self) -> bool:
        return self.name == self.HORROR


class Movie(models.Model):
    name = models.CharField(max_length=512)
    likes = models.IntegerField(default=0)
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return f'{self.name} : {self.id}'
