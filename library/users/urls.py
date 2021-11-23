from django.urls import path

from users.views import UserListAPIView

app_name = 'users'

urlpatterns = [

    path('', UserListAPIView.as_view())

]
