from django.conf.urls import patterns, url
from user_contacts.views import *

urlpatterns = patterns('',
	url(r'^$', home),
	url(r'^all/$', all_contacts),
	url(r'^add/$', add),
	url(r'^create$', create),
)
