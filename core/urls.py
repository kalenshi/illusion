from django.urls import path

from core.employee.detail_view import EmployeeDetailView
from core.employee.list_view import EmployeeListView

app_name = "core"

urlpatterns = [
    path("employees/", EmployeeListView.as_view(), name="employees"),
    path("employees/<emp_no>/", EmployeeDetailView.as_view(),
         name="employee_details"),
]
