from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student, Instructor

class StudentRegistrationForm(UserCreationForm):
    student_id = forms.CharField(max_length=20)
    gender = forms.ChoiceField(choices=Student.GENDER_CHOICES)
    major = forms.CharField(max_length=100)
    contact_number = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'student_id', 'gender', 'major', 'contact_number']

    
class InstructorRegistrationForm(UserCreationForm):
    department = forms.ModelChoiceField(queryset=Department.objects.all())

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'department']
