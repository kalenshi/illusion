from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from core.db_models.employee import Employee
from core.employee.serializers import EmployeeSerializer


class EmployeeDetailView(APIView):
    """
    Methods GET/PATCH/DELETE
    """
    serializer_class = EmployeeSerializer

    def get_object(self, emp_no):
        """
        Retrieve a single object from the database
        """
        try:
            return Employee.objects.get(pk=emp_no)
        except Employee.DoesNotExist:
            raise Http404

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="emp_no",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Employee number",
                required=True,
            ),
        ]
    )
    def get(self, request, emp_no, format=None):
        """
        Retrieve a single employee using emp_no
        """
        employee = self.get_object(emp_no)
        serializer = self.serializer_class(instance=employee)

        return Response(serializer.data, status=status.HTTP_200_OK)
