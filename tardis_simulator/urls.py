from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'tardis_simulator.views.home', name='home'),
	url(r'^chart/$', 'tardis_simulator.views.default_chart', name='chart'),    
)
