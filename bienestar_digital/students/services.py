from .models import Student, Presence, Activity, Schedule, User
from datetime import datetime
from .forms import RegistryStudentForm
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import HttpRequest
from pytz import timezone


# Obtains a Student by request
def get_student(id:str):
    try:
        user = User.objects.filter(username=id).first()
        student = Student.objects.get(identification=user)
        return student
    except ObjectDoesNotExist:
        return None


# Call to the necessary validations and insert an presence of a student to an activity
def mark_presence(student: Student, activity_title: str) -> bool:
    entry_time = datetime.now(tz=timezone("America/Bogota"))

    if can_asist(student, entry_time):
        activity = Activity.objects.filter(title=activity_title).first()
        if activity:
            schedule = get_valid_schedule(entry_time, activity)
            if schedule:
                Presence.objects.create(
                    student=student,
                    activity=activity,
                    date=entry_time.date(),
                    entry_hour=schedule.starts,
                    exit_hour=schedule.ends,
                )
                return True
            else:
                raise Exception(
                    f"No hay horario disponible para {activity.title.lower()} por el momento"
                )
        raise Exception(f"La actividad: {activity_title.lower()}, no existe")
    else:
        raise Exception("El estudiante se encuentra en una actividad")


# this service insert on Student table from a HTML form
def create_student(form: RegistryStudentForm, user: User):
    if form.is_valid():
        data = form.cleaned_data
        try:
            return Student.objects.create(
                identification=user,
                name=data["name"],
                last_name=data["last_name"],
                gender=data["gender"],
                program=data["program"],
                semester=data["semester"],
            )
        except IntegrityError:
            raise Exception("El usuario ya tiene datos existentes")
    else:
        raise Exception("El formulario enviado es inválido")


# This valid if a identified student can asist to an activity
def can_asist(student: Student, hour_entry: datetime) -> bool:
    last_presence = Presence.objects.filter(student=student).last()
    if last_presence:
        if (
            hour_entry.time() <= last_presence.exit_hour
            and hour_entry.day == last_presence.date.day
        ):
            raise IntegrityError("El estudiante aún se encuentra en una actividad")
        else:
            return True
    else:
        return True


# This obtains the available schedule for an identified actvity in a definied datetime
def get_valid_schedule(presence: datetime, activity: Activity) -> Schedule | None:
    activity_schedules = Schedule.objects.filter(activity=activity).all()

    day_presence = presence.strftime("%A").lower()
    hour_presence = presence.time()

    for schedule in activity_schedules:
        if schedule.day.lower() == day_presence:
            if schedule.starts <= hour_presence <= schedule.ends:
                return schedule
    return None


# this returns the student+user object for the students/my-data path
def get_current_student(req: HttpRequest) -> Student:
    user = req.user
    if user.is_authenticated:
        try:
            student = Student.objects.get(identification=user)
            if student:
                return student
            else:
                return None
        except IntegrityError:
            raise Exception('Usuario, aún no tienes datos de estudiante')
    else:
        return None


def update_student(form: RegistryStudentForm, user: User):
    if form.is_valid():
        data = form.cleaned_data
        try:
            student = Student.objects.get(identification=user)
            if student:
                student.name = data["name"]
                student.last_name = data["last_name"]
                student.gender = data["gender"]
                student.program = data["program"]
                student.semester = data["semester"]
                student.save()
            else:
                raise Exception("Imposible, el estudiante no existe")
        except Exception:
            raise Exception("Algún error ha ocurrido")
        pass
    else:
        raise Exception('El formulario no es válido')

def user_is_student(user:User)->bool:
    try:
        student=Student.objects.get(identification=user)
        return student is not None
    except ObjectDoesNotExist:
        return False