from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Assessment)
admin.site.register(AssessmentQuestion)
admin.site.register(QuestionChoices)
