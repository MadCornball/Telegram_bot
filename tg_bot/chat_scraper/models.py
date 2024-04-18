from django.db import models


class ChatManager(models.Manager):
	def all(self):
		return super().all()


class Chat(models.Model):
	title = models.CharField(max_length=255)
	chat_id = models.CharField(max_length=255, unique=True)
	is_channel = models.BooleanField(default=False)
	
	objects = ChatManager()
	
	def __str__(self):
		return self.title


class PostManager(models.Manager):
	def for_chat(self, chat_id):
		return super().filter(chat_id=chat_id).order_by('-created_at')


class Post(models.Model):
	chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
	text = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	
	objects = PostManager()
	
	def __str__(self):
		return f"Post in {self.chat.title} at {self.created_at}"
