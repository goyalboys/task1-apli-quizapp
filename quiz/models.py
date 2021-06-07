from djongo import models

from django.contrib.auth.models import User



class Course(models.Model):
   course_name = models.CharField(max_length=50)
   total_marks = models.PositiveIntegerField()
   #addquestion=models.ForeignKey(Question,on_delete=models.CASCADE)
   #addstudent=models.ForeignKey(studentmail,on_delete=models.CASCADE)
   date = models.DateTimeField(auto_now=True)
   def __str__(self):
        return self.course_name
class Question(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    question_number = models.PositiveIntegerField()
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)
    def __str__(self):
        return self.question
class Result(models.Model):
    #student = models.ForeignKey(Student,on_delete=models.CASCADE)
    exam = models.ForeignKey(Course,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)
class students(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    email=models.EmailField(max_length=254)
#class studentmail(models.Model):
class allow(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    students=models.ForeignKey(students,on_delete=models.CASCADE)