from django.db import models
from django.core.mail import send_mail
from django.conf import settings
import time, threading
from datetime import timedelta, datetime, timezone

# Create your models here.
class Mail(models.Model):
	topic = models.CharField(max_length=254)
	email = models.EmailField(max_length=254)
	message = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	delay = models.SmallIntegerField()

	def __str__(self):
		return self.topic
		
	@property
	def date_delay(self):
		return self.date + timedelta(seconds=self.delay)

	@property
	def send(self):
		if self.date_delay < datetime.now(timezone.utc):
			date = self.date_delay
			return date.strftime('%d.%m.%Y %H:%M:%S')
		else:
			return 'Отправляется'

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		print(self.topic, self.message, self.email, self.date, self.delay)
		def send_mail_delay(topic, message, email, delay, *args, **kwargs):
			time.sleep(delay)
			send_mail(
				topic, 
				message, 
				settings.EMAIL_HOST_USER, 
				[email],
				fail_silently=False)
		t = threading.Thread(target=send_mail_delay, args=(self.topic, self.message, self.email, self.delay,))
		t.start()
