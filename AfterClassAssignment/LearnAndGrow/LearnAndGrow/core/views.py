from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import InstructorRegistrationForm, StudentRegistrationForm

def instructor_registration(request):
    if request.method == 'POST':
        form = InstructorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('core:home')  # Redirect to the home page or dashboard
    else:
        form = InstructorRegistrationForm()
    return render(request, 'instructor_registration.html', {'form': form})

def student_registration(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('core:home')  # Redirect to the home page or dashboard
    else:
        form = StudentRegistrationForm()
    return render(request, 'student_registration.html', {'form': form})


# CREATE TABLE courses (
#     CourseId INT AUTO_INCREMENT PRIMARY KEY,
#     CourseName VARCHAR(255) NOT NULL,
#     Duration VARCHAR(50)
# );
# INSERT INTO enrollments (StudentId, CourseId)
# VALUES
#     (1, 1), 
#     (2, 1), 
#     (1, 2), 
#     (3, 3), 
#     (4, 4); 


# SELECT
#  *
# FROM
#     students s
# JOIN
#     enrollments e ON s.StudentId = e.StudentId
# JOIN
#     courses c ON e.CourseId = c.CourseId;
