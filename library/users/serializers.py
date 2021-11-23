from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class UserModelSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username','email')


class UserModelSerializerWithFullName(ModelSerializer):

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')



