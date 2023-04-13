from django.db import models

class Problem(models.Model):
    level = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=300)
    description = models.TextField()
    input_format = models.CharField(max_length=200)
    output_format = models.CharField(max_length=200)
    hint = models.CharField(max_length=400)
    language = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)