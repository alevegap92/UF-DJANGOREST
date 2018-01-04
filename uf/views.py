# Create your views here.
from rest_framework import viewsets
from uf.models import *
from uf.serializers import *

class UfViewSet(viewsets.ModelViewSet):

    queryset = Uf.objects.all()
    serializer_class = UfSerializer