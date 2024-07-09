from django import forms
from .models import Activity, Program


class AsistenceForm(forms.Form):
    activity = forms.ModelChoiceField(
        queryset=Activity.objects.all(),
        empty_label=None,
        label="Actividad",
        required=True
    )
    identification = forms.CharField(
        label="Identificación",
        required=True,
        widget=forms.TextInput(attrs={"id": "identification"})
    )
    def __init__(self, req=None, *args, **kwargs):
        super(AsistenceForm, self).__init__(*args, **kwargs)
        if req:
            if req.user.is_authenticated:
                user = req.user
                self.fields['identification'].widget.attrs.update({
                    'value':user.username
                })

pass


class RegistryStudentForm(forms.Form):
    name = forms.CharField(
        label="Nombres", widget=forms.TextInput(attrs={"id": "name", 'class': 'form-item'}), required=True
    )
    last_name = forms.CharField(
        label="Apellidos", widget=forms.TextInput(attrs={"id": "last_name", 'class': 'form-item'}),
        required=True
    )
    gender = forms.ChoiceField(
        choices=[("M", "Masculino"), ("F", "Femenino"), ("O", "Otro")],
        label="Género",
        widget=forms.RadioSelect(attrs={"id": "gender", 'class': 'form-item'}),
        required=True
    )
    program = forms.ModelChoiceField(
        queryset=Program.objects.all(), empty_label=None, label="Programa",required=True
    )
    SEMESTER_CHOICES = [
        ("I", "I"),
        ("II", "II"),
        ("III", "III"),
        ("IV", "IV"),
        ("V", "V"),
        ("VI", "VI"),
        ("VII", "VII"),
        ("VIII", "VIII"),
        ("IX", "IX"),
        ("X", "X"),
    ]
    semester = forms.ChoiceField(
        choices=SEMESTER_CHOICES,
        required=True,
        label="Semestre",
        widget=forms.Select(attrs={"id": "semester", 'class': 'form-item'}),
    )

    def __init__(self, *args, **kwargs):
        super(RegistryStudentForm, self).__init__(*args, **kwargs)
        self.fields['program'].widget.attrs.update({
            'class': 'form-item',
            'id':'program',
        })
    pass
pass