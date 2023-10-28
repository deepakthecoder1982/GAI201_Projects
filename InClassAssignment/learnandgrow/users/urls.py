from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router
router = DefaultRouter()

# Register your viewsets with the router
router.register(r'profile', views.UserProfileViewSet, basename='user-profile')
router.register(r'courses', views.CourseViewSet)
router.register(r'departments', views.DepartmentViewSet, basename='department')

# For registration and login, use view functions

urlpatterns = [
    path('register/', views.user_registration, name='user-registration'),
    path('login/', views.user_login, name='user-login'),
    path('enroll-course/', views.enroll_course, name='enroll-course'),
    path('submit-assignment/', views.submit_assignment, name='submit-assignment'),
    path('view-submissions/', views.view_submissions, name='view-submissions'),
    path('raise-ticket/', views.raise_ticket, name='raise-ticket'),
    path('list-departments/', views.list_departments, name='list-departments'),
    path('refresh_token/', views.CustomTokenObtainPairView.as_view(), name='token-refresh'),
    path('', include(router.urls)),  # Include the router's URLs
]
