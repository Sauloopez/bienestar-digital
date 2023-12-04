from .models import Student, Asistence, Activity
from datetime import datetime, timedelta
from .forms import RegistryStudentForm
from django.db import IntegrityError

def get_student(identification:int):
    return Student.objects.filter(identification=identification).first()

def mark_asistence(student, activity_title)-> bool:
    entry_time = datetime.now()
    exit_time = entry_time + timedelta(hours=2)

    activity = Activity.objects.filter(title=activity_title).first()
    if activity:
        Asistence.objects.create(
            student=student,
            activity=activity,
            entry_hour=entry_time,
            exit_hour=exit_time
        )
        return True
    return False

def create_student(form:RegistryStudentForm):
    try:
        student = form.save()
        return student
    except IntegrityError as e:
        raise Exception("Error registrando. La identificación ya tiene datos asociados")