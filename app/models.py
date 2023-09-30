from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Admin'),
        (2, 'Employee')
    )
    user_type = models.IntegerField(choices=USER_TYPE_CHOICES, default=0)


def __str__(self):
    return "CustomUser=" + str(self.user) + ", user_type=" + str(self.user_type)


# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(CustomUser, null=True, blank=True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=35)
    department = models.CharField(max_length=30,
                                  choices=[('development', 'Development'), ('testing', 'Testing'), ('ml', 'Ml')])
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    region = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    zipcode = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "User=" + str(self.user) + ", Email=" + str(self.email) + ", FName=" + str(
            self.first_name) + ", lName=" + str(self.last_name) + ", mobile=" + str(self.mobile) + ", address=" + str(
            self.address) + ", City=" + str(self.city) + ", reigon=" + str(self.region) + ", country=" + str(
            self.country) + ", zip=" + str(self.zipcode)


class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=30,
                                  choices=[('casual leave', 'casual leave'), ('paid leave', 'paid leave'),
                                           ('sick leave', 'sick leave')])
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)
    leave_status = models.CharField(max_length=25, choices=[('1', 'pending'), ('2', 'rejected'), ('3','accepted')], default=1)
    reason = models.TextField(max_length=150, default=None)
