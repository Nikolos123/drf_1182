from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer,StringRelatedField
from .models import Authors,Book,Biography

class AuthorModelSerializer(ModelSerializer):

    class Meta:
        model = Authors
        fields = '__all__'
        # fields = ['first_name']
        # exclude = ['first_name']

class AuthorModelSerializerBase(ModelSerializer):

    class Meta:
        model = Authors
        fields = ('first_name',)


class BookSerializer(ModelSerializer):
    # author = AuthorModelSerializer(many=True)
    class Meta:
        model = Book
        fields = '__all__'

    # def create(self, validated_data):
    #     pass

class BiographyModelSerializer(ModelSerializer):

    class Meta:
        model = Biography
        fields = '__all__'


