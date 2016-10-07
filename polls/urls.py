from django.conf.urls import url

from . import views	# url for view.py

app_name = 'polls'
urlpatterns = [
    # ex: /
    url(r'^$', views.main, name='main'),
    # ex: /
    url(r'^user/$', views.index, name='index'),
    # ex: /steward
    url(r'^steward/$', views.steward, name='steward'),
    # ex: //5/
    url(r'^user/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /5/results/
    url(r'^user/(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /5/vote/
    url(r'^user/(?P<question_id>[0-9]+)/seat/$', views.seat, name='seat'),
]

