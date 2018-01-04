from rest_framework import serializers
from uf.models import *

class UfSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Uf
        fields = ('value', 'date')	