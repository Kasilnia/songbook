from django.conf.urls import url

from main.views import SongBookView


urlpatterns = [
    url(r'^$', SongBookView.as_view(), name='home'),
]
