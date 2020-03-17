from rest_framework import serializers

from .models import *

class AssessmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Assessment

    fields = ('id', 'title', 'created_at', 'deadline')

class AssessmentQuestionSerializer(serializers.ModelSerializer):
  class Meta:
    model = AssessmentQuestion

    fields = ('id', 'assessment_id', 'question_text', 'answer')

class QuestionChoicesSerializer(serializers.ModelSerializer):
  class Meta:
    model = QuestionChoices

    fields = ('id', 'question_id', 'alias', 'choice_text')