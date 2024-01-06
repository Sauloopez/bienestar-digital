from django import forms
from .models import Activity, Program, Student


class AsistenceForm(forms.Form):
    activity = forms.ModelChoiceField(
        queryset=Activity.objects.all(),
        empty_label=None,
        label="Actividad",
        required=True
    )
    identification = forms.IntegerField(
        label="Identificación",
        required=True,
        widget=forms.NumberInput(attrs={"id": "identification"}),
    )
    pass


class RegistryStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['identification', 'name', 'last_name', 'gender', 'program', 'semester']

    name = forms.CharField(
        label="Nombres", widget=forms.TextInput(attrs={"id": "name"}), required=True
    )
    last_name = forms.CharField(
        label="Apellidos", widget=forms.TextInput(attrs={"id": "last_name"}),
        required=True
    )
    identification = forms.IntegerField(
        label="Identificación",
        widget=forms.NumberInput(attrs={"id": "identification"}),
        required=True
    )

    gender = forms.ChoiceField(
        choices=[("M", "Masculino"), ("F", "Femenino"), ("O", "Otro")],
        label="Género",
        widget=forms.RadioSelect(attrs={"id": "gender"}),
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
        widget=forms.Select(attrs={"id": "semester"}),
    )

