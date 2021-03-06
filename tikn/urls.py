"""tikn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from apps.books.views import BookList, BookDetail
from apps.pages.views import PageDetail

admin.site.site_header = 'Administracja Tikn'

urlpatterns = [
    url(r'^$', BookList.as_view(), name='book-list'),
    url(r'^book/(?P<slug>[-\w]+)/$', BookDetail.as_view(), name='book-detail'),
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<slug>[-\w]+)/$', PageDetail.as_view(), name='page-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
