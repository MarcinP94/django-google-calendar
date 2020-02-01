from django.test import SimpleTestCase
from django.urls import reverse, resolve
from event.views import home, delete, MyEvent, sync, create, update


class TestUrls(SimpleTestCase):

    def test_home_url(self):
        url = reverse('event:home')
        self.assertEquals(resolve(url).func, home)

    def test_sync_url(self):
        url = reverse('event:sync')
        self.assertEquals(resolve(url).func, sync)

    def test_my_event_url(self):
        url = reverse('event:my_events')
        self.assertEquals(resolve(url).func.view_class, MyEvent)

    def test_create_url(self):
        url = reverse('event:new')
        self.assertEquals(resolve(url).func, create)

    def test_delete_url(self):
        url = reverse('event:delete', args=['1'])
        self.assertEquals(resolve(url).func, delete)

    def test_update_url(self):
        url = reverse('event:update', args=['1'])
        self.assertEquals(resolve(url).func, update)




