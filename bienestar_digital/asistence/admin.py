from django.contrib import admin
from .models import Program, Student, Activity, Asistence, Schedule

# Register your models here.
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title',)  # Muestra el título en la lista de objetos en el panel de administración

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('identification', 'name', 'last_name', 'gender', 'program', 'semester')
    search_fields = ('identification', 'name', 'last_name')  # Agrega campos de búsqueda
    list_filter = ('program', 'semester')  # Agrega filtros en el panel de administración

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')
    list_filter = ('id', 'title')  # Agrega filtros en el panel de administración

@admin.register(Asistence)
class AsistenceAdmin(admin.ModelAdmin):
    list_display = ('student', 'activity')

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('activity', 'starts', 'ends')