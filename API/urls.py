from django.urls import path
from .views import MessageView,GetUnreadMSG

urlpatterns = [
    path('message/', MessageView.as_view(), name='message'),
    path('GetUnreadMSG/', GetUnreadMSG.as_view(), name='GetUnreadMSG'),
]