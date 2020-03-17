from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

# Create your views here.

class AssessmentView(viewsets.ModelViewSet):
  serializer_class = AssessmentSerializer
  queryset = Assessment.objects.all()

class AssessmentQuestionView(viewsets.ModelViewSet):
  serializer_class = AssessmentQuestionSerializer
  queryset = AssessmentQuestion.objects.all()

class QuestionChoicesView(viewsets.ModelViewSet):
  serializer_class = QuestionChoicesSerializer
  queryset = QuestionChoices.objects.all()