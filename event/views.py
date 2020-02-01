from event.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  View
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import ModelForm
from apiclient.discovery import build
import pickle
from event.API import GoogleCalendar



class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'start', 'end','event_id']


def home(request):
    return render(request, 'event/main.html')


def create(request, template_name='event/form.html'):
    """ Function which add new record to database and to google calendar"""
    form = PostForm(request.POST or None)
    if form.is_valid():
        title = form.data['title']
        start_time = form.data['start']
        end_time = form.data['end']
        GoogleCalendar.sent_to_API(title, start_time, end_time)

        """ assign event id to event_id filed"""
        replace = form.save(commit=False)
        replace.event_id = GoogleCalendar.get_event_id()
        replace.save()
        form.save()
        return redirect('event:home')
    return render(request, template_name, {'form': form})


class MyEvent(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):

        events = Post.objects.all()
        context = {
                'object': events
                 }
        return render(self.request, 'event/my_events.html', context)


def delete(request, pk, template_name='event/confirm_delete.html'):
    my_event = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        GoogleCalendar.delete_from_API(my_event.event_id)
        my_event.delete()
        return redirect('event:my_events')
    return render(request, template_name, {'object': my_event})


def update(request, pk, template_name='event/form.html'):
    calendar = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=calendar)
    if form.is_valid():
        GoogleCalendar.edit_to_API(calendar.title, calendar.start, calendar.end, calendar.event_id)
        form.save()
        return redirect('event:my_events')
    return render(request, template_name, {'form': form})


def sync(request):
    """ Establish synchronization """
    model = Post.objects.all()
    for element in model:
        model_event_id = element.event_id  #get event_id form database
        model_id = element.id # get id record
        calendar = get_object_or_404(Post, pk=model_id)
        form = PostForm(request.POST or None, instance=calendar)  # get form for element
        """ Get element from google calendar"""
        credentials = pickle.load(open("token.pkl", "rb"))
        service = build("calendar", "v3", credentials=credentials)
        result = service.calendarList().list().execute()
        calendar_id = result['items'][0]['id']
        my_event = service.events().get(calendarId=calendar_id, eventId=model_event_id).execute()

        """ Update element from google calendar to website"""
        element.start = my_event['start']['dateTime']
        replace = form.save(commit=False)
        replace.title = my_event['summary']
        replace.start = my_event['start']['dateTime']
        replace.end = my_event['end']['dateTime']
        replace.save()

    return redirect('event:my_events')

