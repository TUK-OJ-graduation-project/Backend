from rest_framework import serializers
from .models import Solution
from problems.models import Problem

class SolutionSerializer(serializers.ModelSerializer):
    problem = serializers.PrimaryKeyRelatedField(queryset=Problem.objects.all())

    class Meta:
        model = Solution
        fields = ['id', 'problem', 'source_code', 'created_at', 'updated_at', 'is_accepted']
        read_only_fields = ['id', 'created_at', 'updated_at']

