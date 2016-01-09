from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    graduation = models.DateTimeField()


class Transcript(models.Model):
    student = models.ForeignKey(Student)

    def gpa(self):
        credits = 0
        grade_points = 0
        for period in self.period_set.all():
            for course in period.course_set.all():
                credits += course.credits
                grade_points += course.grade_points() * course.credits

        return grade_points / credits

class Period(models.Model):
    transcript = models.ForeignKey(Transcript)
    year = models.IntegerField()
    month = models.IntegerField()

    def title(self):
        season = "Fall"
        if self.month == 3:
            season = "Spring"
        if self.month == 6:
            season = "Summer"
        return "Semester of {}-{}".format(self.year, season)

    def average(self):
        credits = 0
        grade_points = 0
        for course in self.course_set.all():
            credits += course.credits
            grade_points += course.grade_points() * course.credits

        if credits == 0:
            print("Failure!", self.id)
        return grade_points/credits

    def passing_average(self):
        return self.average() > 1.0

class Course(models.Model):
    period = models.ForeignKey(Period)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    credits = models.IntegerField()

    def passing_grade(self):
        if self.grade != 'F':
            return True
        return False

    def grade_points(self):
        return {
            'A+': 4.3,
            'A': 4.0,
            'A-': 3.7,
            'B+': 3.3,
            'B': 3.0,
            'B-': 2.7,
            'C+': 2.3,
            'C': 2.0,
            'C-': 1.7,
            'D+': 1.3,
            'D': 1.0,
            'D-': 0.7,
            'F': 0
            }[self.grade]
