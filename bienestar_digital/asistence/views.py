from django.shortcuts import render, redirect
from .forms import AsistenceForm, RegistryStudentForm
from .services import get_student, mark_asistence, create_student
from django.db import IntegrityError
# Create your views here.

def asistence(req):
    method = req.method
    #method get shows HTML form
    if method == 'GET':
        return render(req, 'asistence.html', {
            'form' : AsistenceForm
        })
    #Method post is allowed for receive the data-form
    elif method == 'POST':
        form = AsistenceForm(req.POST)
        if form.is_valid():
            #If the identification is relationed with an student, obtains an Student
            student = get_student(form.cleaned_data['identification'])
            activity = form.cleaned_data['activity']
            if student is not None:
                try:
                    #if student exists, mark he/his asistence into Asistence
                    if mark_asistence(student, activity):
                        #Returns with a gratified message if can assist
                        return render(req, 'asistence.html',{
                            'message': 'Asistencia guardada'
                        })
                except Exception as e:
                    # Shows a bad message if the student cannot asist
                    return render(req, 'asistence.html', {
                        'message': str(e)
                    })
            else:
                #If the student does not exist, returns an error message
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
        if form:
            try:
                #create a student from the FormModel
                create_student(form=form)
                return render(req, 'registry_student.html', {
                    'message': 'Datos insertados satisfactoriamente.'
                })
            except Exception as e:
                #If create a student raise an exception and shows the error message
                return render(req, 'registry_student.html',{
                    'form':RegistryStudentForm,
                    'error': str(e)
                })
        else:
            #if the form not is valid, shows an error
            return render(req, 'registry_student.html',{
                    'form':RegistryStudentForm,
                    'error': "El formulario es inválido"
                })
    pass