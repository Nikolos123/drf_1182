from rest_framework.permissions import AllowAny,DjangoModelPermissionsOrAnonReadOnly
from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from .models import Authors,Biography,Book
from .serializers import AuthorModelSerializer,BiographyModelSerializer,BookSerializer

class AuthorModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Authors.objects.all()
    serializer_class = AuthorModelSerializer
    # permission_classes =  [AllowAny]

    # def create(self, request, *args, **kwargs):
    #
    # def destroy(self, request, *args, **kwargs):
    #
    # def list(self, request, *args, **kwargs):
    #
    # def update(self, request, *args, **kwargs):


class BiographyModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer

class BookModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
