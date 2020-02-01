from django.test import TestCase
from django.urls import reverse, resolve
from event.models import Post
from datetime import datetime, timedelta

class TestModels(TestCase):
    def setUp(self):
        pass

    def test_title_string_representation(self):
        event = Post(title="My entry title")
        self.assertEqual(str(event), event.title)





