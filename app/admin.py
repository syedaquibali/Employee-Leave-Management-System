
from django.contrib import admin
from django.contrib.auth.models import User

from .models import *

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Employee)
admin.site.register(LeaveRequest)



