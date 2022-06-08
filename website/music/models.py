from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=300)
    surname = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Song(models.Model):
    title = models.CharField(max_length=1000)
    created_at = models.DateField()
    authors = models.ManyToManyField(Author, blank=True)

    def __str__(self):
        return self.title
