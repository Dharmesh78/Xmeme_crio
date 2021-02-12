from django.urls import path
from appCRIO import views
from django.conf import settings # new
app_name='appCRIO'
urlpatterns=[
    path('',views.memeListAPI,name='addDisplayMemes'),
    path('<int:pk>/',views.memeDetailAPI,name='editShowMeme'),
    path('memeDelete/<int:pk>/', views.memeDelete,name='deleteMeme'),
]


#
# curl --location --request POST 'http://127.0.0.1/memes' \
#
# --header 'Content-Type: application/json' \
#
# --data-raw '{
#         "name": "NEWname22",
#         "mcaption": "NEWcaption22",
#         "meme_url": "https://api.memegen.link/images/money/shut_up_and/take_my_money!.jpg?width=300"
#     }'
