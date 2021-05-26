from rest_framework.exceptions import NotFound

from core.employee.serializers import Employee, EmployeeSerializer
from core.salaries.serializers import SalariesSerializer


class ProfilesDomain:
    """
    Provides functionality for creating /retrieving Employee profiles
    """

    def get_profile(self, emp_no):
        """Get the an employees profile"""

        try:
            data = {}
            employee = Employee.objects.get(pk=emp_no)
            emp_serializer = EmployeeSerializer(instance=employee)
            data["employee"] = emp_serializer.data
            sal_serializer = SalariesSerializer(employee.get_salaries(),
                                                many=True)
            data["employee"]["salaries"] = sal_serializer.data

            return data

        except Employee.DoesNotExist:
            raise NotFound(f"Employee id {emp_no} Does not exist")
