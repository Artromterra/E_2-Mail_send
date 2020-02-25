from django.urls import path 
from .views import MailList, MailCreate

app_name = 'mail'
urlpatterns = [
	path('', MailCreate.as_view(), name='mail_create'),
	path('mail_list/', MailList.as_view(), name='mail_list'),
]