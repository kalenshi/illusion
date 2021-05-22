from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from core.db_models.employee import Employee
from core.employee.serializers import EmployeeSerializer


class EmployeeListView(APIView):
    """
    Methods : GET/POST
    """
    serializer_class = EmployeeSerializer

    def get(self, request, format=None):
        """
        Used to get a list of Employees

        Returns: Employees
        """
        queryset = Employee.objects.all()
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)