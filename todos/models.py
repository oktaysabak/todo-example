from django.db import models

class Todo(models.Model):
    """Todo model class."""
    detail = models.CharField(max_length=255, null=False)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='todos', on_delete=models.CASCADE)

    def __str__(self) -> str:
        """Object representaion method to show first 10 character of todo detail."""
        return f'{self.detail[:10]}+{"..."}' 
