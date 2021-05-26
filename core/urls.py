from django.urls import path

from core.employee.detail_view import EmployeeDetailView
from core.employee.list_view import EmployeeListView
from core.profiles.detail_view import EmployeeProfileDetailView
from core.profiles.list_view import EmployeeProfileListView
from core.salaries.detail_view import SalariesDetailView
from core.salaries.list_view import SalariesListView

app_name = "core"

urlpatterns = [
    path("employees/", EmployeeListView.as_view(), name="employees"),
    path(
        "employees/<emp_no>/",
        EmployeeDetailView.as_view(),
        name="employee_details"
    ),
    path("salaries/", SalariesListView.as_view(), name="salaries"),
    path(
        "salaries/<emp_no>/",
        SalariesDetailView.as_view(),
        name="salaries_details"
    ),
    path("profiles/", EmployeeProfileListView.as_view(), name="profiles"),
    path("profiles/<emp_no>/", EmployeeProfileDetailView.as_view(),
         name="profiles")
]
