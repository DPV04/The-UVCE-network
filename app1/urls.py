from django.urls import path
from . import views
from django.conf import settings

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 


urlpatterns=[
    path('home/',views.home,name='home'),
    path('room/<str:pk>/',views.rom,name='room'),
    path('createroom/',views.enterroomdetails,name='enterroomdetails'),
    # path('updateroom/<str:pk>/',views.updateroom,name='updateroom'),
    path('deleteroom/<str:pk>/',views.deleteroom,name='deleteroom'),
    path('register/', views.register, name='register'),
    path('login/', views.logunpage, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('deletemessge/<str:pk>/',views.deletemessages,name='deletemessage'),
    path('userprofile/<str:pk>/',views.userprofile,name='userprofile'),
    path('upload/<str:pk>/',views.uploads,name='upload'),
    path('userdetails/',views.interest,name='interests'),
    path('feed/',views.feeds,name='feed'),
    path('userupdate/',views.updateUser,name='userupdate'),


]


MEDIA_URL = '/media/'
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

    urlpatterns +=staticfiles_urlpatterns()