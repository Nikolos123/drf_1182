from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer,StringRelatedField
from .models import Authors,Book,Biography

class AuthorModelSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Authors
        fields = '__all__'
        # fields = ['first_name']
        # exclude = ['first_name']


class BookModelSerializer(ModelSerializer):
    author = AuthorModelSerializer(many=True)
    class Meta:
        model = Book
        fields = '__all__'

class BiographyModelSerializer(ModelSerializer):

    class Meta:
        model = Biography
        fields = '__all__'


