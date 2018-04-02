from django.conf.urls import patterns, include, url
from django.contrib import admin
from cms import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.pagina_inicial, name = 'pagina_inicial'),
    url(r'^recurso/(\d+)$', views.pagina, name = 'recursos'),
    url(r'^admin/', include(admin.site.urls)),
)
