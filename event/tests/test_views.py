from django.test import TestCase, Client
from django.urls import reverse
from event.models import Post
from datetime import datetime, timedelta

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home = reverse('event:home')
        self.my_events = reverse('event:my_events')
        self.create = reverse('event:new')

        self.delete = reverse('event:delete', args=['1'])
        self.update = reverse('event:update', args=['1'])
        time = datetime(2020, 1, 25, 19, 30, 0)
        time1 = time + timedelta(hours=4)
        self.project = Post.objects.create(title = "test", start =time.strftime("%Y-%m-%dT%H:%M:%S"),
        end = time1.strftime("%Y-%m-%dT%H:%M:%S"), event_id = "N/A")

    def test_home_GET(self):
        response = self.client.get(self.home)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'event/main.html')
        self.assertEquals(response.status_code, 200)



# GET / POST NEW
# GET / POST DELETE
# GET / POST UPDATE
# GET SYNC
