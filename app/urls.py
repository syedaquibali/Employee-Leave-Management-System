from django.urls import path

from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('user_login/', views.user_login, name='user_login'),
    path('logout/', views.logout, name='logout'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('employee_dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('employee_list/', views.employee_list, name='employee_list'),
    path('add_employee/', views.add_employee, name='add_employee'),

    path("delete-employee/<int:user_id>", views.delete_employee, name='delete_employee'),
    path("update-employee/<int:user_id>", views.update_employee, name='update_employee'),

    path("apply_leave/", views.apply_leave, name='apply_leave'),
    path("leave_report/", views.leave_report, name='leave_report'),
    path("delete_employee_leave/<int:id>", views.delete_employee_leave, name='delete_employee_leave'),
    path("update_employee_leave/<int:id>", views.update_employee_leave, name='update_employee_leave'),
    path("all_leave_request/", views.all_leave_request, name='all_leave_request'),

    path("accept_leave/<int:id>", views.accept_leave, name='accept_leave'),
    path("reject_leave/<int:id>", views.reject_leave, name='reject_leave'),

]