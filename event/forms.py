from django import forms
from event.models import Post


class Event(forms.ModelForm):

    class Meta:

        model = Post
        fields = ['title', 'start', 'end', 'event_id']




