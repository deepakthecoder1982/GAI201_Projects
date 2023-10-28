from rest_framework import viewsets, status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from .models import CustomUser
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from .models import Course,Department,Submission
from .serializers import CourseSerializer,DepartmentSerializer,CustomUserSerializer,AssignmentSerializer,SubmissionSerializer,EnrollmentSerializer,TicketSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

@api_view(['POST'])
@authentication_classes([])  # No authentication required for registration
@permission_classes([])  # No permission required for registration
def user_registration(request):
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            # Extract the role from the request data
            role = request.data.get('role', 'student')  # Default role is 'student'
            if role not in ('student', 'instructor', 'admin'):
                return Response({'message': 'Invalid role'}, status=status.HTTP_400_BAD_REQUEST)

            # Hash the user's password
            password = make_password(serializer.validated_data['password'])
            serializer.validated_data['password'] = password

            # Create the user with the specified role
            user = serializer.save(role=role)

            # Create a token for the user
            token, created = Token.objects.get_or_create(user=user)

            response_data = {
                'user_id': user.pk,
                'email': user.email,
                'token': token.key,  # Include the token in the response
                'role': role,  # Include the role in the response
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
@authentication_classes([])  # No authentication required for login
@permission_classes([])  # No permission required for login
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            # Get or create a token for the user
            token, created = Token.objects.get_or_create(user=user)

            response_data = {
                'user_id': user.pk,
                'email': user.email,
                "role": user.role,
                'token': token.key,  # Include the token in the response
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])  # Token authentication required
@permission_classes([IsAuthenticated])  # Only authenticated users can access profile

def user_profile(request):
    user = request.user  # The authenticated user
    if request.method == 'GET':
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        logout(request)  # Log the user out after deletion
        return Response({'message': 'User deleted'}, status=status.HTTP_204_NO_CONTENT)

class UserProfileViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]  # Token authentication required
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        user = request.user
        serializer = CustomUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user = request.user
        user.delete()
        logout(request)  # Log the user out after deletion
        return Response({'message': 'User deleted'}, status=status.HTTP_204_NO_CONTENT)



class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    authentication_classes = []  # No authentication required for listing departments
    permission_classes = []  # No permission required for listing departments

    def create(self, request, *args, **kwargs):
        # Create a new department
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@authentication_classes([])  # No authentication required for listing departments
@permission_classes([])  # No permission required for listing departments
def list_departments(request):
    departments = Department.objects.all()
    serializer = DepartmentSerializer(departments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])  # Token authentication required
@permission_classes([IsAuthenticated])  # Only authenticated users can enroll
def enroll_course(request):
    if request.method == 'POST':
        # Check if the user is a student
        if request.user.role != 'student':
            return Response({'message': 'Only students can enroll in courses'}, status=status.HTTP_403_FORBIDDEN)

        serializer = EnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            # Ensure the student_id matches the authenticated user
            if serializer.validated_data['student_id'] == request.user.student.id:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Invalid student ID'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])  # Token authentication required
@permission_classes([IsAuthenticated])  # Only authenticated users can submit assignments
def submit_assignment(request):
    if request.method == 'POST':
        # Check if the user is a student
        if request.user.role != 'student':
            return Response({'message': 'Only students can submit assignments'}, status=status.HTTP_403_FORBIDDEN)

        serializer = SubmissionSerializer(data=request.data)
        if serializer.is_valid():
            # Ensure the student_id matches the authenticated user
            if serializer.validated_data['student_id'] == request.user.student.id:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Invalid student ID'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])  # Token authentication required
@permission_classes([IsAuthenticated])  # Only authenticated users can view submissions
def view_submissions(request):
    if request.method == 'GET':
        # Check if the user is a student
        if request.user.role != 'student':
            return Response({'message': 'Only students can view submissions'}, status=status.HTTP_403_FORBIDDEN)

        student_id = request.user.student.id
        submissions = Submission.objects.filter(student_id=student_id)
        serializer = SubmissionSerializer(submissions, many=True)
        return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])  # Token authentication required
@permission_classes([IsAuthenticated])  # Only authenticated users can raise tickets
def raise_ticket(request):
    if request.method == 'POST':
        # Check if the user is a student
        if request.user.role != 'student':
            return Response({'message': 'Only students can raise tickets'}, status=status.HTTP_403_FORBIDDEN)

        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            # Ensure the student_id matches the authenticated user
            if serializer.validated_data['student_id'] == request.user.student.id:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Invalid student ID'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CustomTokenObtainPairView(TokenObtainPairView):
    pass

