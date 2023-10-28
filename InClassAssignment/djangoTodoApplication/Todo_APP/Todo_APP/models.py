from django.db import models

# class TodoModel(models.Model):
#     title = models.CharField(max_length=50)
#     description = models.CharField(max_length=100)
#     status = models.CharField(
#         max_length=20,
#         default="NotStarted",
#         choices=(
#             ("InProgress", "InProgress"),
#             ("Completed", "Completed"),
#             ("NotStarted", "NotStarted")
#         )
#     )

#     def __str__(self):
#         return self.title  # This is optional, but it will make the object more readable

#     class Meta:
#         app_label = "todo"  # This might not be necessary if you don't have a specific reason for it
