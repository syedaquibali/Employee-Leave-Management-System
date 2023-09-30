from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth

from app.models import Employee, CustomUser, LeaveRequest


# Create your views here.


def home(request):

    return render(request, 'home.html')


def admin_dashboard(request):

    return render(request, 'admin_dashboard.html')

def employee_dashboard(requst):

    return render(requst, 'employee_dashboard.html')

def employee_list(request):
    employee = Employee.objects.all()
    context ={
        'employee': employee,
    }
    return render(request, 'employee_list.html', context)

def add_employee(request):
    if request.method == 'POST':
        print("Added")

        # retrieve the user input

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        designation = request.POST.get('designation')
        department = request.POST.get('department')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        city = request.POST.get('city')
        region = request.POST.get('region')
        zipcode = request.POST.get('zipcode')
        country = request.POST.get('country')


        # <!-- Roll_no validation Unique --!>
        isExist = Employee.objects.filter(mobile=mobile).exists()
        emailExist = Employee.objects.filter(email=email).exists()

        error_message = None
        if isExist:
            error_message = "Mobile number is Already Exist"
        elif emailExist:
            error_message = "Email Address is Already Exist"

        if not error_message:

            user = CustomUser.objects.create_user(username=email, email=email, password=password)
            user.user_type= 2
            user.save()


            # create an object for models
            s = Employee()
            s.user = user
            s.first_name = first_name
            s.last_name = last_name
            s.email = email
            s.designation = designation
            s.department = department
            s.mobile = mobile
            s.address = address
            s.city = city
            s.region = region
            s.zipcode = zipcode
            s.country = country

            s.save()
            return redirect('/employee_list')
        else:
            context = {
                'error': error_message
            }
        return render(request, 'add_employee.html', context)
    return render(request, 'add_employee.html')

def admin_login(request):
    if request.method == 'GET':
        return render(request, 'admin_login.html')

    else:
        # retrieve the user input
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(request.POST)
        print(email, password)

        user = auth.authenticate(username=email, password=password)
        #user = CustomUser.objects.get(email=email)
        print('----------')
        print(user)
        print('----------')
        if user is not None and user.user_type==1:
            auth.login(request, user)
            return redirect("/admin_dashboard/")
        else:
            error_message = "Please Enter Correct username and Password"

            return render(request, 'admin_login.html', {'error': error_message})

    return render(request, 'admin_login.html')

def user_login(request):
    if request.method == 'GET':
        return render(request, 'user_login.html')

    else:
        # retrieve the user input
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(request.POST)
        print(email, password)

        user = auth.authenticate(username=email, password=password)
        # user = CustomUser.objects.get(email=email)
        print('----------')
        print(user)
        print('----------')
        if user is not None and user.user_type ==2:
            auth.login(request, user)
            return redirect("/employee_dashboard/")
        else:
            error_message = "Please Enter Correct username and Password"

            return render(request, 'user_login.html', {'error': error_message})

    return render(request, 'user_login.html')

def delete_employee(request, user_id):
    s=Employee.objects.get(pk=user_id)
    s.delete()

    return redirect("/employee_list/")

def update_employee(request, user_id):
    user = CustomUser.objects.get(pk=user_id)
    employee = Employee.objects.get(user=user)


    if request.method=='POST':

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        designation = request.POST.get('designation')
        department = request.POST.get('department')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        city = request.POST.get('city')
        region = request.POST.get('region')
        zipcode = request.POST.get('zipcode')
        country = request.POST.get('country')


        user.email = email
        user.username = email

        user.save()

        employee.first_name = first_name
        employee.last_name = last_name
        employee.designation = designation
        employee.department = department
        employee.mobile = mobile
        employee.address = address
        employee.city = city
        employee.region = region
        employee.zipcode = zipcode
        employee.country = country

        employee.save()
        return redirect('/employee_list')

    return render(request, "update_employee.html",{'user':user, 'employee' : employee})

def logout(request):
    auth.logout(request)
    return redirect('/')

# "--------------------------------------------------"

def apply_leave(request):
    print("---------------------")

    print(request.user.id)
    print("666699999999999999")

    emp=Employee.objects.get(user_id=request.user.id)
    print("############")
    print(emp)
    print("---------------")



    if request.method=='POST':
        print(request.POST)
        leave_type = request.POST.get('leave_type')
        reason = request.POST.get('reason')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')



        #object create for leaveRequest class#

        leave_request= LeaveRequest()
        leave_request.leave_type = leave_type
        leave_request.reason = reason
        leave_request.start_date = start_date
        leave_request.end_date = end_date
        leave_request.leave_status = "1"
        leave_request.employee = emp

        leave_request.save()
        return redirect('/leave_report/')

    return render(request,'apply_leave.html')

def leave_report(request):
    employee= Employee.objects.get(user_id=request.user.id)
    leave_report= LeaveRequest.objects.filter(employee=employee).order_by('-id')
    context = {
        'leave_report': leave_report,
    }

    return render(request,'leave_report.html', context)

def delete_employee_leave(request, id):
    s=LeaveRequest.objects.get(pk=id)
    s.delete()

    return redirect("/leave_report")


def update_employee_leave(request, id):
    leave=LeaveRequest.objects.get(pk=id)

    if request.method=='POST':
        print(request.POST)
        leave_type = request.POST.get('leave_type')
        reason = request.POST.get('reason')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')


        leave.leave_type = leave_type
        leave.reason = reason
        leave.start_date = start_date
        leave.end_date = end_date

        leave.save()
        return redirect('/leave_report')

    return render(request, 'update_employee_leave.html', {'leave': leave})


def all_leave_request(request):
    all_leave= LeaveRequest.objects.filter(leave_status='1').order_by('-id')
    context ={
        'all_leave': all_leave
    }

    return render(request, 'all_leave_request.html', context)

def accept_leave(request, id):
    l = LeaveRequest.objects.get(pk=id)
    l.leave_status = "3"
    l.save()

    return redirect('/all_leave_request/')


def reject_leave(request, id):
    m = LeaveRequest.objects.get(pk=id)
    m.leave_status = "2"
    m.save()

    return redirect('/all_leave_request/')