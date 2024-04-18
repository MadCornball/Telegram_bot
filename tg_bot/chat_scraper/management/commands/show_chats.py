import os
import sys
import django
from django.core.management.base import BaseCommand
from Telegram_bot.tg_bot.chat_scraper.services import get_all_chats, get_paginated_posts_for_chat

# Добавляем текущий путь к приложению Django в sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Инициализируем Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tg_bot.settings')
django.setup()

class Command(BaseCommand):
    help = 'Show all chats and posts in JSON format.'

    def handle(self, *args, **kwargs):
        chats = get_all_chats()
        for chat in chats:
            self.stdout.write(self.style.SUCCESS(f'Chat: {chat.title} (ID: {chat.id})'))
            posts = get_paginated_posts_for_chat(chat.id)
            self.stdout.write(self.style.SUCCESS('Posts:'))
            for post in posts:
                self.stdout.write(self.style.SUCCESS(f'  - {post.text}'))
