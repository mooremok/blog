from django.db import models
from note.models import Note

class Comments(models.Model):
    nickname = models.CharField(max_length=20)
    email = models.EmailField()
    content = models.TextField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)
    target = models.ForeignKey(Note, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
    
    class Meta:
        ordering = ['-created_time']
