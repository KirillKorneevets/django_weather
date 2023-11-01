from django.db import models


class Message(models.Model):
    chat_id = models.CharField(max_length=255, null=True, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    sender = models.CharField(max_length=255, choices=[('admin', 'Admin'), ('user', 'User')], default='user')

    def __str__(self):
        return f"Chat id - {self.chat_id}"

    def save(self, *args, **kwargs):
        if self.sender == 'admin':
            self.sender = 'admin'
        else:
            self.sender = 'user'
        super(Message, self).save(*args, **kwargs)

    class Meta:
        db_table = 'message'


