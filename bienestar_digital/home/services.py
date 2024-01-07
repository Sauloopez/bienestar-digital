from students.models import Activity, Schedule, User
from .forms import RegistryForm, LoginForm
from django.db import IntegrityError
from django.contrib.auth import login, authenticate
from itertools import repeat

def get_activities():
    activities = Activity.objects.all()
    activities_dict = {}
    for activity in activities:
        activities_dict[activity.id]={
            'object': activity,
            'schedule':get_schedule_for_activity(activity)
        }
    return activities_dict

def get_schedule_for_activity(activity: Activity):
    days_of_week = ['L', 'K', 'M', 'J', 'V', 'S']

    schedule_dict = {day: dict(zip(range(8, 19+1), repeat(False))) for day in days_of_week}

    schedules =Schedule.objects.filter(activity=activity)
    if schedules:
        for schedule in schedules:
            day= get_day_letter(schedule.day.lower())
            if 19 > schedule.starts.hour >= 8 and 8 < schedule.ends.hour <= 19:
                for i in range(schedule.starts.hour, schedule.ends.hour):
                    schedule_dict[day][i] = True
                pass
            pass
        pass
    return schedule_dict

def get_day_letter(day:str):
    days = {
        'monday':'L',
        'tuesday':'K',
        'wednesday':'M',
        'thursday':'J',
        'friday':'V',
        'saturday':'S'
    }
    return days[day]

def create_user(form:RegistryForm)->User:
    if form.is_valid():
        try:
            form.clean()
            new_user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            new_user.save()
            return new_user
        except IntegrityError:
            raise Exception(f"El usuario {form.cleaned_data['username']} ya tiene datos relacionados")
    else:
        raise Exception(f"Las contraseñas no son iguales")

def user_access(req, form: LoginForm):
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user:
            login(req, user)
        else:
            raise Exception('Credenciales Inválidas')
    else:
        raise Exception('El formulario es inválido')