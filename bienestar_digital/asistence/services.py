from .models import Student, Asistence, Activity, Schedule
from datetime import datetime, timedelta
from .forms import RegistryStudentForm
from django.db import IntegrityError
from pytz import timezone
import pytz

#Obtains a Student by identification
def get_student(identification:int):
    return Student.objects.filter(identification=identification).first()


#Call to the necessary validations and insert an asistence of a student to an activity
def mark_asistence(student:Student, activity_title:str)-> bool:
    entry_time = datetime.now(tz=timezone('America/Bogota'))

    if can_asist(student, entry_time):
        activity = Activity.objects.filter(title=activity_title).first()
        if activity:
            schedule = get_valid_schedule(entry_time, activity)
            if schedule:
                Asistence.objects.create(
                    student=student,
                    activity=activity,
                    date=entry_time.date(),
                    entry_hour=schedule.starts,
                    exit_hour=schedule.ends,
                )
                return True
            else:
                raise Exception(f"No hay horario disponible para {activity.title.lower()} por el momento")
        raise Exception(f"La actividad: {activity_title.lower()}, no existe")
    else:
        raise Exception("El estudiante se encuentra en una actividad")


#this service insert on Student table from a HTML form
def create_student(form:RegistryStudentForm):
    if get_student(int(form.data['identification'])):
        raise Exception("Error al registrar. La identificación ya tiene datos asociados")
    else:
        return form.save()


#This valid if a identified student can asist to an activity
def can_asist(student:Student, hour_entry:datetime)->bool:
    last_asistence = Asistence.objects.filter(student=student).last()
    print(last_asistence.exit_hour, last_asistence.date, hour_entry)
    if last_asistence:
        if hour_entry.time() <= last_asistence.exit_hour and hour_entry.day == last_asistence.date.day:
            raise IntegrityError("El estudiante aún se encuentra en una actividad")
        else:
            return True
    else:
        return True


#This obtains the available schedule for an identified actvity in a definied datetime
def get_valid_schedule(asistence:datetime, activity:Activity)-> Schedule | None:
    activity_schedules = Schedule.objects.filter(activity=activity).all()

    day_asistence = asistence.strftime("%A").lower()
    hour_asistence = asistence.time()
    
    for schedule in activity_schedules:
        if schedule.day.lower() == day_asistence:
            if schedule.starts <= hour_asistence <= schedule.ends:
                return schedule
    return None