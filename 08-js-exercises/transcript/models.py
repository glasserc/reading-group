from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    graduation = models.DateTimeField()


class Transcript(models.Model):
    student = models.ForeignKey(Student)


class Period(models.Model):
    transcript = models.ForeignKey(Transcript)
    year = models.IntegerField()
    month = models.IntegerField()


class Course(models.Model):
    period = models.ForeignKey(Period)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    credits = models.IntegerField()
