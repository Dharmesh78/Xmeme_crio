from django.urls import path
from appCRIO import views
from django.conf import settings # new
app_name='appCRIO'
urlpatterns=[
    path('',views.appCRIO,name='apiOverview'),
    path('memesList',views.memeList,name='memesList'),
    path('memeEdit/<int:pk>/',views.memeEdit,name='editMeme'),
    path('memeCreate/', views.memeCreate,name='addMeme'),
    path('memeDelete/<int:pk>/', views.memeDelete,name='deleteMeme'),
]
