from .models import Chat, Post


def get_all_chats():
    """
    Возвращает список всех чатов и каналов.
    """
    return Chat.objects.all()


def get_posts_for_chat(chat_id):
    """
    Возвращает все посты для указанного чата.
    """
    return Post.objects.filter(chat_id=chat_id).order_by('-created_at')


def get_paginated_posts_for_chat(chat_id, page_number=1, page_size=10):
    """
    Возвращает отсортированные по времени появления посты для указанного чата
    с пагинацией.
    """
    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size
    posts = Post.objects.filter(chat_id=chat_id).order_by('-created_at')[start_index:end_index]
    return posts


def create_chat(title, chat_id, is_channel=False):
    """
    Создает новый чат или канал.
    """
    return Chat.objects.create(title=title, chat_id=chat_id, is_channel=is_channel)


def create_post(chat_id, text):
    """
    Создает новый пост в указанном чате.
    """
    chat = Chat.objects.get(chat_id=chat_id)
    return Post.objects.create(chat=chat, text=text)
