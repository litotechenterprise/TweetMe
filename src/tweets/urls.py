from django.urls import path, re_path
from .views import TweetListView, TweetDetailView, TweetCreateView, TweetUpdateView, TweetDeleteView

app_name = 'tweets'
urlpatterns = [
    path('', TweetListView.as_view(), name='list'), #/tweets/
    path('create/', TweetCreateView.as_view(), name='create'), #/tweets/create/
    re_path(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'), #/tweets/pk/
    re_path(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'), #/tweets/pk/update/
    re_path(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'), #/tweets/pk/delete/      
]
