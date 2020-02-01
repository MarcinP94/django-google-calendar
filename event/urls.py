from . import views
from django.conf.urls import url
from django.urls import path

app_name = "event"
urlpatterns = [

    url(r'^$', views.home, name='home'),
    path('new/', views.create, name='new'),
    url(r'^my_events/$', views.MyEvent.as_view(), name='my_events'),
    path('my_events/delete/<int:pk>', views.delete, name='delete'),
    path('my_events/update/<int:pk>', views.update, name='update'),
    path('sync/', views.sync, name='sync'),
]
