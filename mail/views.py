from django.shortcuts import redirect, render
from .forms import MailForm
from django.views.generic import ListView, CreateView
from .models import Mail
from django.urls import reverse_lazy


# Create your views here.


class MailCreate(CreateView):
	model = Mail
	form_class = MailForm
	success_url = reverse_lazy('mail:mail_list')
	template_name = 'mail_create.html'

class MailList(ListView):
	model = Mail
	mail = Mail.objects.all()
	template_name = 'mail_list.html'