from django.urls import path
from frontend import views
from django.conf import settings # new
app_name='frontend'
urlpatterns=[
    path('',views.list,name='list'),
]
