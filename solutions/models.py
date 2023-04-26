from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Solution(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    source_code = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_accepted = models.BooleanField(default=False) # 올바른 출력값(output)을 낸다면 True. (테스트케이스로 채점결과 반영)
    
    # 다양한 문제 유형을 처리하기 위한 Generic foreign key
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    problem = GenericForeignKey('content_type', 'object_id')
    
