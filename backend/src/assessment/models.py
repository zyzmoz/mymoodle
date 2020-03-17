from django.db import models

# Create your models here.
class Assessment(models.Model):
  title = models.CharField(max_length=120)
  description = models.CharField(max_length=120)
  created_at = models.DateTimeField(auto_now=True)
  deadline = models.DateTimeField()
  # created_by = models.ForeignKey()  

  def __str__(self):
    return self.title


class AssessmentQuestion(models.Model):
  assessment_id = models.ForeignKey(Assessment, on_delete=models.CASCADE)
  question_text = models.CharField(max_length=500)  
  answer = models.CharField(max_length=2)

  def __str__(self):
    return self.question_text

class QuestionChoices(models.Model):
  question_id = models.ForeignKey(AssessmentQuestion, on_delete=models.CASCADE)
  alias = models.CharField(max_length=2)
  choice_text = models.CharField(max_length=120)

  def __str__(self):
    return "{}. {}".format(self.alias, self.choice_text)


