from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Permission, Group
from django.db import models

class Department(models.Model):
    de_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    groups = models.ManyToManyField(Group, blank=True, related_name='custom_users')
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='custom_users'
    )

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=20)
    major = models.CharField(
        max_length=20,
        choices=[
            ('Computer Science', 'Computer Science'),
            ('Engineering', 'Engineering'),
            ('Business', 'Business'),
            # Add other majors here
        ]
    )
    contact_number = models.CharField(max_length=15)
    # Add any other student-specific fields

class Instructor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    instructor_id = models.CharField(max_length=20)
    department = models.CharField(
        max_length=20,
        choices=[
            ('Science', 'Science'),
            ('Arts', 'Arts'),
            ('Computer Science', 'Computer Science'),
            # Add other departments here
        ]
    )
    date_of_birth = models.DateField()
    # Add any other instructor-specific fields
     
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    credits = models.PositiveIntegerField()
    description = models.TextField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.course_id) 

class Admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # Add any admin-specific fields

# Assignment models

class Assignment(models.Model):
    assign_id = models.AutoField(primary_key=True) 
    title = models.CharField(max_length=50)
    Description = models.TextField()
    Due_Date = models.DateTimeField(auto_now_add=True)
    Course_id = models.ForeignKey(Course,on_delete=models.CASCADE)

# subsmission models

class Submission(models.Model):
    submis_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    Assignment_id = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    Submission_date = models.DateTimeField(auto_now_add=True)


# Enrollment

class Enrollment(models.Model):
    Enrollment_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    Enrollment_date = models.DateTimeField(auto_now_add=True)

# Tickets 

class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('resolved', 'Resolved'),
            ('not-resolved', 'not-resolved'),
            # Add other majors here
        ]
    )
    create_date = models.DateTimeField(auto_created=True)
    resolve_date = models.DateTimeField(auto_created=True)
