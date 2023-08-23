from django.db import models

# class ToDo(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     completed = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

class ToDo:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed
