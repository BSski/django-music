from django.test import TestCase
from datetime import date
from music.models import Song, Author


class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_author = Author.objects.create(
            name="TestName",
            surname="TestSurname",
        )

    def test_author_str_equals_name_and_surname(self):
        self.assertEqual(
            str(self.test_author), f"{self.test_author.name} {self.test_author.surname}"
        )


class SongModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_song = Song.objects.create(
            title="TestTitle",
            created_at=date(2022, 6, 8),
        )

    def test_song_str_equals_song_title(self):
        self.assertEqual(str(self.test_song), self.test_song.title)

    def test_song_has_an_author(self):
        test_author = Author.objects.create(
            name="TestName",
            surname="TestSurname",
        )
        self.test_song.authors.set([test_author])

        self.assertEqual(self.test_song.authors.count(), 1)
