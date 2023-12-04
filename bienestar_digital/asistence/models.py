from django.db import models

# Create your models here.

class Program(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.title
    pass

class Student(models.Model):
    identification = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    gender = models.CharField(max_length=2, null=False)
    program = models.ForeignKey(Program, on_delete=models.DO_NOTHING)
    semester = models.CharField(max_length=5,null=False)
    def __str__(self) -> str:
        return str(self.identification)
    pass

class Activity(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    instructor = models.CharField(max_length=300)
    def __str__(self) -> str:
        return self.title
    pass

class Asistence(models.Model):
    id_asistence = models.BigAutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    activity = models.ForeignKey(Activity, on_delete=models.DO_NOTHING)
    entry_hour = models.DateTimeField()
    exit_hour = models.DateTimeField()
    pass