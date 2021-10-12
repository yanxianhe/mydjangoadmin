"""mydjangoadmin URL Configuration

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
from . import views
from mydjangoadmin.check import check_views
from mydjangoadmin.fileclass import file_views
from mydjangoadmin.api.authentication import login_views
urlpatterns = [
    ### api
    # 重写认证 待写
    # aip login authentication
    url(r'^api/login', login_views.login_api),
    url(r'^api/logout', login_views.logout_api),

    ### 首页
    url(r'^$', views.ping),
    url(r'^admin/', admin.site.urls),
    url(r'^check/', check_views.check),
    url(r'^upload_file/', file_views.upload_file),



]
