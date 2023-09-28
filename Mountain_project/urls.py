"""Mountain_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Mountain_app  import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name='index'),
    path('ab', views.ab , name='ab'),
    path('cd', views.cd , name='cd'),
    path('ef', views.ef , name='ef'),
    path('gh', views.gh , name='gh'),
    path('ij', views.ij , name='ij'),
    path('yatra', views.yatra_add , name='yatra'),
    path('ottp', views.ottp , name='ottp'),
    path('otp_vrify', views.otp_vrify , name='otp_vrify'),
    path('home', views.home , name='home'),
    path('signup', views.signup , name='signup'),
    path('logout', views.logout , name='logout'),
    path('help', views.help , name='help'),
    path('story_form', views.story_form , name='story_form'),
    path('all_story', views.all_story , name='all_story'),
    path('login', views.login , name='login'),
    path('gallary', views.gallary , name='gallary'),
    path('resend_otp', views.resend_otp , name='resend_otp'),
    path('register_guide', views.register_guide , name='register_guide'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
