from django.http import JsonResponse
from .models import Chat

def chat_list(request):
    chats = Chat.objects.all()
    data = [{'id': chat.id, 'name': chat.name} for chat in chats]
    return JsonResponse(data, safe=False)
