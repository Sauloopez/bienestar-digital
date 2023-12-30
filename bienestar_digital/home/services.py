from asistence.models import Activity, Schedule

def get_activities():
    return Activity.objects.all()