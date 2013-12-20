from django.conf.urls import patterns, url

from UserContacts.views import *

urlpatterns = patterns('',
	url(r'^$', home),
    url(r'^all/$', all_contacts),
    url(r'^add/$', add),
    url(r'^create$', create),
)
