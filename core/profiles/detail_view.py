from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.profiles.domain import ProfilesDomain as Domain


class EmployeeProfileDetailView(APIView):
    """List of employee profile Details"""

    def get(self, request, emp_no, format=None):
        """
        Responsible for retrieving an employee profile
        """
        domain = Domain()
        employee_profile = domain.get_profile(emp_no)

        return Response(employee_profile, status=status.HTTP_200_OK)

