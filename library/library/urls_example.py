"""libraty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

# from authors.views import AuthorViewSet,BookViewSet,BiographyViewSet
# from libraty.view_example import BookViewSet
# from libraty.view_example import BookListAPIView


# from library.view_example import get
# from library.view_example import BookViewSet, BookLimitOffsetPaginatonViewSet

router = DefaultRouter()
# from library.view_example import BookModelViewSet
# from library.view_example import BookModelViewSet

# router = SimpleRouter()
# router.register('authors', AuthorViewSet)
router.register('book_p', BookLimitOffsetPaginatonViewSet)
# router.register('biography', BiographyViewSet)


# from library.view_example import BookCreateAPIView,BookRetrieveAPIView,BookDestroyAPIView,BookListAPIView,BookUpdateAPIView

# router.register('create', BookCreateAPIView)
# # router.register('biography', BookRetrieveAPIView)
# # router.register('biography', BookDestroyAPIView)
# # router.register('biography', BookListAPIView)
# # router.register('biography', BookUpdateAPIView)

# level 3
# router.register('book', BookViewSet,basename='book')

# level 4
# router.register('book', BookViewSet)

# level 5
# router.register('books', BookCustomViewSet)

#Filter
# router.register('book_filter', BookQuerysetFilterViewSet)


#
router.register('book', BookViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/', include(router.urls)),

    # level 1
    # path('api/', BookAPIView.as_view()),
    # path('api/', get),

    # level 2
    # path('api/list/', BookListAPIView.as_view()),
    # path('api/create/', BookCreateAPIView.as_view()),
    # path('api/update/<int:pk>/', BookUpdateAPIView.as_view()),
    # path('api/delete/<int:pk>/', BookDestroyAPIView.as_view()),
    # path('api/detail/<int:pk>/', BookRetrieveAPIView.as_view()),

    # # level 3 - 5
    # path('api/', include(router.urls)),

    # filter part_2
    # path('api/filters/kwargs/<str:name>/', BookListAPIView.as_view()),
    #
    path('api/', include(router.urls)),


]
