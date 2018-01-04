from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from uf import views

#from django_filters.views import FilterView
#from uf.models import *

uf_list = views.UfViewSet.as_view({
    'get': 'list',
})


urlpatterns = [
    url(r'^list/$', uf_list, name='uf-list'),
    #url(r'^search/$', FilterView.as_view(model=Uf)),
]

urlpatterns = format_suffix_patterns(urlpatterns)  	