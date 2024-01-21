from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Program(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.title
pass

class Student(models.Model):
    identification = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True
    )
    name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    gender = models.CharField(max_length=2, null=False)
    program = models.ForeignKey(Program, on_delete=models.DO_NOTHING)
    semester = models.CharField(max_length=5, null=False)

    def __str__(self) -> str:
        return str(self.identification)
pass


class Activity(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    instructor = models.CharField(max_length=300)
    img = models.CharField(max_length=300)
    def __str__(self) -> str:
        return self.title
pass

class Asistence(models.Model):
    id_asistence = models.BigAutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    activity = models.ForeignKey(Activity, on_delete=models.DO_NOTHING)
    date = models.DateField()
    entry_hour = models.TimeField()
    exit_hour = models.TimeField()

    @classmethod
    def create_dict_from_db(cls) -> dict:
        rows = cls.objects.select_related('student__identification', 'student__program', 'activity')
        values = rows.values(
            'id_asistence',
            'activity__title',
            'student__identification__username',
            'student__name',
            'student__last_name',
            'student__program__title',
            'student__semester',
            'entry_hour',
            'exit_hour'
        )
        return list(values)
pass

class Schedule(models.Model):
    id_schedule = models.CharField(max_length=20, primary_key=True)
    activity = models.ForeignKey(Activity, on_delete=models.DO_NOTHING)
    day = models.CharField(max_length=20)
    starts = models.TimeField()
    ends = models.TimeField()
    def __str__(self) -> str:
        return self.id_schedule