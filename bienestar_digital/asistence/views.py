from django.shortcuts import render, redirect
from .forms import AsistenceForm, RegistryStudentForm
from .services import get_student, mark_asistence, create_student
# Create your views here.

def asistence(req):
    method = req.method
    if method == 'GET':
        return render(req, 'asistence.html', {
            'form' : AsistenceForm
        })
    elif method == 'POST':
        form = AsistenceForm(req.POST)
        if form.is_valid():
            student = get_student(form.cleaned_data['identification'])
            activity = form.cleaned_data['activity']
            if student is not None:
                if mark_asistence(student, activity):
                    return render(req, 'asistence.html',{
                        'message': 'Asistencia guardada'
                    })
            else:
                return render(req, 'asistence.html', {
                    'error': 'Aún no te has registrado en este semestre. ' 
                })
    pass

def registry_student(req):
    method = req.method
    if method == 'GET':
        return render(req, 'registry_student.html',{
            'form': RegistryStudentForm
        })
    elif method == 'POST':
        form = RegistryStudentForm(req.POST)
        if form.is_valid():
            try:
                create_student(form=form)
                return render(req, 'registry_student.html', {
                    'message': 'Datos insertados satisfatoriamente.'
                })
            except Exception as e:
                return render(req, 'registry_student.html',{
                    'form':RegistryStudentForm,
                    'error': str(e)
                })
        else:
            return render(req, 'registry_student.html',{
                    'form':RegistryStudentForm,
                    'error': form.errors
                })
    pass