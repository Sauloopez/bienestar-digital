from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AsistenceForm, RegistryStudentForm
from .services import (
    get_student,
    mark_asistence,
    get_current_student,
    create_student,
    update_student as update_student_serv,
    user_is_student,
)

# Create your views here.


def asistence(req):
    method = req.method
    form = AsistenceForm(req=req)
    # method get shows HTML form
    if method == "GET":
        return render(req, "asistence.html", {"form": form})
    # Method post is allowed for receive the data-form
    elif method == "POST":
        form = AsistenceForm(data=req.POST)
        if form.is_valid():
            # If the identification is relationed with an student, obtains an Student
            student = get_student(form.cleaned_data["identification"])
            activity = form.cleaned_data["activity"]
            if student is not None:
                try:
                    # if student exists, mark he/his asistence into Asistence
                    if mark_asistence(student, activity):
                        # Returns with a gratified message if can assist
                        return render(
                            req,
                            "asistence.html",
                            {
                                "message": "Asistencia guardada",
                                "form": form,
                            },
                        )
                except Exception as e:
                    # Shows a bad message if the student cannot asist
                    return render(
                        req,
                        "asistence.html",
                        {"message": str(e), "form": AsistenceForm},
                    )
            else:
                # If the student does not exist, returns an error message
                return render(
                    req,
                    "asistence.html",
                    {
                        "error": "Aún no te has registrado en este semestre. ",
                        "form": AsistenceForm,
                    },
                )
    pass


@login_required()
def student_data_view(req):
    try:
        student = get_current_student(req)
        form = RegistryStudentForm(
            {
                "name": student.name,
                "last_name": student.last_name,
                "gender": student.gender,
                "program": student.program,
                "semester": student.semester,
            }
        )
        return render(
            req,
            "student_data.html",
            {
                "student": student,
                "form": form,
            },
        )
    except Exception as e:
        return render(
            req, "registry_student.html", {"form": RegistryStudentForm, "error": e}
        )


@login_required()
def registry_data_student(req):
    method = req.method
    if method == "GET":
        form = RegistryStudentForm
        if not user_is_student(req.user):
            return render(req, "registry_student.html", {"form": form})
        else:
            return redirect("/students/my-data")

    if method == "POST":
        form = RegistryStudentForm(req.POST)
        try:
            create_student(form, req.user)
            return redirect("/students/my-data")
        except Exception as e:
            return render(
                req,
                "registry_student.html",
                {
                    "form": form,
                    "error": e.with_traceback,
                },
            )
    pass


def update_student(req):
    method = req.method
    if method == "GET":
        form = RegistryStudentForm
        return render(req, "student_data.html", {"form": form})
    elif method == "POST":
        form = RegistryStudentForm(req.POST)
        try:
            update_student_serv(form, req.user)
            return redirect("/students/my-data")
        except Exception as e:
            return render(
                req, "registry_student.html", {"form": form, "error": e.with_traceback}
            )


pass
