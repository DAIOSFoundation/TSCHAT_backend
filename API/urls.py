from django.urls import path
from .views import MessageView,GetUnreadMSG

urlpatterns = [
    path('SendMessage/', MessageView.as_view(), name='SendMessage'),
    path('GetUnreadMSG/', GetUnreadMSG.as_view(), name='GetUnreadMSG'),
]