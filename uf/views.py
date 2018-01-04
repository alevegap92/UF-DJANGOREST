# Create your views here.
from rest_framework import viewsets
from uf.models import *
from uf.serializers import *
from django_filters import rest_framework as filters


class UfFilter(filters.FilterSet):
    class Meta:
        model = Uf
        fields = ['value', 'date']

class UfViewSet(viewsets.ModelViewSet):

    queryset = Uf.objects.all()
    serializer_class = UfSerializer
    filter_class = UfFilter
