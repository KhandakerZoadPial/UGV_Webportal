from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout', views.logout_view, name='logout'),
    path('login', views.student_login, name='login'),
    path('studentPortal', views.student_portal, name='student_portal'),
    path('Admission_office', views.admission_office_portal, name='Admission_office'),
    path('admission_office_login', views.admission_office_login, name='admission_office_login'),
    path('admit_a_student', views.admit_a_student, name='admit_a_student'),
    path('change_pass', views.change_pass, name='change_pass'),
    path('Course_Notes', views.Course_Notes, name='Course_Notes'),
    path('acounts_section', views.accounts_section, name='accounts_section'),
    path('Registration', views.Registration, name='Registration'),
    path('results', views.results, name='results'),
    path('My_Personal_Notes', views.My_Personal_Notes, name='My_Personal_Notes')
]