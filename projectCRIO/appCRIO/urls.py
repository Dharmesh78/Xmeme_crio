from django.urls import path
from appCRIO import views
from django.conf import settings # new
app_name='appCRIO'
urlpatterns=[
    path('',views.memeListAPI,name='addDisplayMemes'),
    path('/',views.memeListAPI,name='addDisplayMemes'),
    path('<int:pk>/',views.memeDetailAPI,name='editShowMeme'),
    path('memeDelete/<int:pk>/', views.memeDelete,name='deleteMeme'),
]
