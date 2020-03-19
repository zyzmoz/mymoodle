from django.db import models

# Create your models here.
class Assignment(models.Model):
  title = models.CharField(max_length=120)
  text = models.TextField()
  # user_id = models.ForeignKey();

  def __str__(self):
    return self.title

class AssignmentAnswers(models.Model):
  # student_id = models.ForeignKey()
  assignment_id = models.ForeignKey(Assignment, on_delete=models.CASCADE)
  file = models.FileField()
  text = models.TextField()

  # def __str__(self):
  #   return self.id



