from django.test import TestCase
from datetime import date
from music.models import Song

#
# class SongModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.test_song = Song(
#             id="1",
#             title="TestTitle",
#             authors=["TestAuthor"],
#             created_at=date(2022, 3, 22),
#         )
#
#     def test_song_str_equals_song_title(self):
#         self.assertEqual(str(self.test_song), self.test_song.title)
#
#
# class AuthorModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.test_author = Author(
#             id="1",
#             name="TestName",
#             surname="TestSurname",
#         )
#
#     def test_author_str_equals_name_and_surname(self):
#         self.assertEqual(str(self.test_author), f"{self.name} {self.surname}")
