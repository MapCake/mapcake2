from django.conf.urls import patterns, include, url
from django.contrib import admin

from home.views import home
from layers.views import layers_list

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'mapcake.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^$', home, name='home'),
                       url(r'^layers/', 'layers.views.layers_list', name='layers'),

                       # url(r'^admin/', include(admin.site.urls)),
                       )
