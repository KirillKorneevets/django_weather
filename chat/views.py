from django.shortcuts import redirect, render
from .models import Message
from django.views.generic.base import View
from django import forms




class ChatView(View):

    def post(self, request, chat_id):
        message_content = request.POST.get('message', '')
        message = Message(content=message_content, chat_id=chat_id)
        message.save()
        return redirect('chat_view', chat_id=chat_id)

    def get(self, request, chat_id):
        messages = Message.objects.filter(chat_id=chat_id, active=True)
        return render(request, 'chat.html', {'messages': messages, 'chat_id': chat_id})



class StartChatForm(forms.Form):
    question = forms.CharField(label='Опишите ваш вопрос', max_length=255)


class StartChat(View):

    def post(self, request):
        form = StartChatForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            message = Message(chat_id=question, content=question)
            message.save()
            return redirect('chat_view', chat_id=question)

    def get(self, request):
        form = StartChatForm()
        return render(request, 'start_chat.html', {'form': form})
