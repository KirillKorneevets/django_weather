from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_filter = ('timestamp', 'active')
    actions = ['delete_all_by_chat_id']

    def delete_all_by_chat_id(self, request, queryset):
        chat_id = queryset.first().chat_id
        Message.objects.filter(chat_id=chat_id).delete()
    
    delete_all_by_chat_id.short_description = "Delete all messages by chat_id"