from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from uf import views

uf_list = views.UfViewSet.as_view({
    'get': 'list',
})


urlpatterns = [
    url(r'^$', uf_list, name='uf-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)  	