from django.shortcuts import render

# Create your views here.
from rest_framework.authtoken.admin import User
from rest_framework.generics import ListAPIView

from users.serializers import UserModelSerializer, UserModelSerializerWithFullName




class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    # serializer_class = UserModelSerializer


    def get_serializer_class(self):
        if self.request.version == 'v2':
            return UserModelSerializerWithFullName
        return UserModelSerializer