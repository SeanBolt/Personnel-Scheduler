from django.conf.urls import url, include
from . import views

app_name = 'results'

urlpatterns = [
	# ex: /
	url(r'^$', views.surveys),
]