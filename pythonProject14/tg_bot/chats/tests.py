import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tg_bot.tg_bot.settings')
import django
django.setup()

from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Chat



class ChatListViewTestCase(TestCase):
	def setUp(self):
		self.client = APIClient()
		self.user_chats = [
			Chat.objects.create(name='User Chat 1'),
			Chat.objects.create(name='User Chat 2'),
			Chat.objects.create(name='User Group 1', is_group=True),
			Chat.objects.create(name='User Group 2', is_group=True)
		]
	
	def test_chat_list_view(self):
		url = reverse('chat-list')
		response = self.client.get(url)
		
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 4)  # Всего 4 чата: 2 чата и 2 группы
