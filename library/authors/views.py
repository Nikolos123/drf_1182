from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from .models import Authors
from .serializers import AuthorModelSerializer

class AuthorModelViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
    queryset = Authors.objects.all()
    serializer_class = AuthorModelSerializer