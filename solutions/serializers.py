from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from .models import Solution
from problems.models import CodingProblem, OptionProblem, BlankProblem

class ProblemRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        if isinstance(value, CodingProblem):
            return f'CodingProblem: {value.title}'
        elif isinstance(value, OptionProblem):
            return f'OptionProblem: {value.title}'
        elif isinstance(value, BlankProblem):
            return f'BlankProblem: {value.title}'
        else:
            raise Exception('Unexpected problem type')

    def to_internal_value(self, data):
        # Split the data string by ':'
        type, problem_id = data.split(':')
        problem_id = int(problem_id.strip())

        if type == 'CodingProblem':
            return CodingProblem.objects.get(id=problem_id)
        elif type == 'OptionProblem':
            return OptionProblem.objects.get(id=problem_id)
        elif type == 'BlankProblem':
            return BlankProblem.objects.get(id=problem_id)
        else:
            raise Exception('Unexpected problem type')

class SolutionSerializer(serializers.ModelSerializer):
    problem = ProblemRelatedField(queryset=ContentType.objects.none())

    class Meta:
        model = Solution
        fields = ['id', 'problem', 'source_code', 'created_at', 'updated_at', 'is_accepted']
        read_only_fields = ['id', 'created_at', 'updated_at']


