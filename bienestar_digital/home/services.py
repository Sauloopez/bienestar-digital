from asistence.models import Activity, Schedule
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

    schedule_dict = {day: dict(zip(range(6, 22+1), repeat(False))) for day in days_of_week}

    schedules =Schedule.objects.filter(activity=activity)
    if schedules:
        for schedule in schedules:
            day= get_day_letter(schedule.day.lower())
            
            for i in range(schedule.starts.hour, schedule.ends.hour):
                schedule_dict[day][i] = True
            pass
        pass
        return schedule_dict
    else:
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

    