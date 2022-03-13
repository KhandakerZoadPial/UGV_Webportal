from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Notes


def accounts_logout(request):
    logout(request)
    return redirect('/')


def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and len(user.username)>5:
            auth.login(request, user)
            messages.success(request, 'Successfully logged in.')
            return redirect('/studentPortal')
        else:
            messages.error(request, 'Please provide valid credentials!')
            return redirect('/login')
    else:
        if request.user.is_authenticated:
            messages.error(request, 'You are already logged in.')
            return redirect('/studentPortal')
        return render(request, 'AuthApp/login.html')


def admission_office_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if len(username) > 5:
            messages.error(request, 'Sorry, Something went wrong')
            return redirect('/Admission_office')
        user = authenticate(username=username, password=password)
        if request.user.is_authenticated:
            messages.error(request, 'You are already logged in.')
            return redirect('/Admission_office')

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Successfully logged in.')
            return redirect('/Admission_office')
        else:
            messages.error(request, 'Please provide valid credentials!')
            return redirect('/login')
    else:
        return render(request, 'AuthApp/admission_office_login.html')


def teacher_login(request):
    pass

def home(request):
    return render(request, 'AuthApp/home.html')


def student_portal(request):
    if request.user.is_authenticated:
        user_ = request.user
        if len(user_.username) > 5:
            user_profile = StudentProfile.objects.get(owner=user_)
            context = {
                'profile': user_profile
            }
            return render(request, 'AuthApp/studentPortal.html', context)
        else:
            return redirect('/login')
    else:
        return redirect('/login')


def admission_office_portal(request):
    if request.user.is_authenticated:
        # x = StudentProfile.objects.all()
        return render(request, 'AdmissionOffice/admission_home.html')
    else:
        return render(request, 'AuthApp/admission_office_login.html')


from .models import StudentProfile
def admit_a_student(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            if len(request.user.username) <= 5:
                first_name = request.POST.get('f_name')
                last_name = request.POST.get('l_name')
                date_of_birth = request.POST.get('dob')
                gender = request.POST.get('genderbox')
                address = request.POST.get('stu_address')
                contact_number = request.POST.get('contact_number')
                hsc_background = request.POST.get('hsc_background')
                HSC_Registration_Number = request.POST.get('hsc_reg_number')
                hsc_passing_year = request.POST.get('hsc_year')
                Program = request.POST.get('program')
                local_guardian_name = request.POST.get('gurdian_name')
                local_guardian_relation = request.POST.get('gurdian_relation')
                local_guardian_contact_number = request.POST.get('gurdian_contact_number')
                local_guardian_address = request.POST.get('gurdian_address')
                marksheet = request.FILES.get('marksheet')
                student_photo = request.FILES.get('student_image')

                print(student_photo)
                username_ = str(id_generator())
                password = username_
                student_id = password
                pial = User(username=username_)
                pial.set_password(username_)
                pial.first_name = first_name
                pial.last_name = last_name
                pial.save()

                student_profile_temp_obj = StudentProfile(owner=pial, student_id=student_id, date_of_birth=date_of_birth, gender=gender, address=address, contact_number=contact_number,
                hsc_background=hsc_background, HSC_Registration_Number=HSC_Registration_Number, hsc_passing_year=hsc_passing_year, Program=Program, local_guardian_name=local_guardian_name,
                local_guardian_relation=local_guardian_relation, local_guardian_contact_number=local_guardian_contact_number, local_guardian_address=local_guardian_address,
                marksheet=marksheet, student_photo=student_photo)
                student_profile_temp_obj.save()
                
                messages.success(request, f'Student Admitted Successfully with Student ID: {student_profile_temp_obj.student_id}')
                return render(request, 'AdmissionOffice/admission_home.html')
                
            else:
                return redirect('/admission_office_login')
        else:
            return redirect('/admission_office_login')
    else:
        return redirect('/Admission_office')


from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return redirect('/')


def change_pass(request):
    if request.user.is_authenticated:
        user_ = request.user
        old = request.POST.get('old_pass')
        pass1 = request.POST.get('pass1')

        if user_.check_password(old):
            user_.set_password(pass1)
            user_.save()
            messages.success(request, 'Password Changed Successfully!')
            return redirect('/studentPortal')
        else:
            messages.error(request, 'Wrong Password!')
            return redirect('/studentPortal')
    else:
        return redirect('/login')


def Course_Notes(request):
    if request.user.is_authenticated:
        user_ = request.user
        if len(user_.username) > 5:
            user_profile = StudentProfile.objects.get(owner=user_)
            context = {
                'profile': user_profile
            }
            return render(request, 'AuthApp/course_notes.html', context)
        else:
            return redirect('/login')
    else:
        return redirect('/login')
    


def accounts_section(request):
    if request.user.is_authenticated:
        user_ = request.user
        if len(user_.username) > 5:
            user_profile = StudentProfile.objects.get(owner=user_)
            context = {
                'profile': user_profile
            }
            return render(request, 'AuthApp/accounts_section.html', context)
        else:
            return redirect('/login')
    else:
        return redirect('/login')


def Registration(request):
    if request.user.is_authenticated:
        user_ = request.user
        if len(user_.username) > 5:
            user_profile = StudentProfile.objects.get(owner=user_)
            context = {
                'profile': user_profile
            }
            return render(request, 'AuthApp/Registration.html', context)
        else:
            return redirect('/login')
    else:
        return redirect('/login')


def results(request):
    if request.user.is_authenticated:
        user_ = request.user
        if len(user_.username) > 5:
            user_profile = StudentProfile.objects.get(owner=user_)
            context = {
                'profile': user_profile
            }
            return render(request, 'AuthApp/result.html', context)
        else:
            return redirect('/login')
    else:
        return redirect('/login')


def My_Personal_Notes(request):
    if request.user.is_authenticated:
        user_ = request.user
        if len(user_.username) > 5:
            user_profile = StudentProfile.objects.get(owner=user_)
            if request.method == 'POST':
                title = request.POST.get('title')
                description = request.POST.get('desc')
                notes = Notes(owner=request.user, title=title, description=description)
                notes.save()
            notes_obj = Notes.objects.filter(owner=request.user)
            context = {
                'profile': user_profile,
                'notes': notes_obj
            }
            return render(request, 'AuthApp/My_Personal_Notes.html', context)
        else:
            return redirect('/login')
    else:
        return redirect('/login')
# ----------------------Helpers---------------------
from . models import id_tracker
def id_generator():
    while True:
        x = id_tracker.objects.filter()[0]
        y = StudentProfile.objects.filter(student_id=x.position+1)
        if y.count()==0:
            update_position()
            return str(x.position+1)
        else:
            continue

def update_position():
    x = id_tracker.objects.filter()[0]
    x.position = x.position+1
    x.save()