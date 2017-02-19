from django.conf.urls import url
from .example import views as example_views


urlpatterns = [
    url(r'^$', example_views.example, name='example'),
]
