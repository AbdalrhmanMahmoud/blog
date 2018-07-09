from django.conf.urls import url
from django.contrib import admin

from .views import (
	post_list,
	post_create,
	# post_create,
	post_detail,
	post_update,
	post_delete,
	#nave  pages
	about,
	art,
	sport,
	success,
	comic,
	policy,
	)

urlpatterns = [
	url(r'^$', post_list, name="list"),
    url(r'^create/$', post_create),
    url(r'^detail/(?P<id>\d+)/$', post_detail, name="detail"),
	url(r'^update/(?P<id>\d+)/$', post_update, name="update"),
	url(r'^delete/(?P<id>\d+)/$', post_delete, name="delete"),
	url(r'^about/$', about, name="about"),
	url(r'^art/$', art, name="art"),
	url(r'^sport/$', sport, name="sport"),
	url(r'^success/$', success, name="success"),
	url(r'^comic/$', comic, name="comic"),
	url(r'^policy/$', policy, name="policy"),

	#url(r'^posts/$', "<appname>.views.<function_name>"),
]