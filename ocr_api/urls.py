from django.conf.urls import include, url
from django.contrib import admin
from . import view

urlpatterns = [
    # Examples:
    # url(r'^$', 'ocr_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', view.index),
    url(r'^upload/', view.upload),
    url(r'^hello/', view.hello),
]
