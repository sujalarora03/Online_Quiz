from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.IntegerField()
    password = models.CharField(max_length=500)

    def __str__(self):
        return f'Student: Username-{self.username} Password-{self.password}'
# Added option in question. Changes made in html and views also
class Question_DB(models.Model):
    #added question number for help in question paper
    qno = models.AutoField(primary_key=True)
    question = models.CharField(max_length=100)
    optionA = models.CharField(max_length=100)
    optionB = models.CharField(max_length=100)
    optionC = models.CharField(max_length=100)
    optionD = models.CharField(max_length=100)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return f'Question No.{self.qno}: {self.question} \t\t Options: \nA. {self.optionA} \nB.{self.optionB} \nC.{self.optionC} \nD.{self.optionD} '

class Question_Paper(models.Model):
    
    qPaperTitle = models.CharField(max_length=100) 
    questions = models.ManyToManyField(Question_DB)
    
    def __str__(self):
        return f' Queston Paper Title :- {self.qPaperTitle}\n'