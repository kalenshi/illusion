from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from core.db_models.employee import Employee
from core.employee.serializers import EmployeeSerializer


class EmployeeListView(APIView):
    """
    Methods : GET/POST

    Lists all Employees or creates a new Employee
    """
    serializer_class = EmployeeSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="hire_date",
                description="The day the Employee got Hired",
                required=False,
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING
            )
        ]
    )
    def get(self, request, format=None):
        """
        Used to get a list of Employees

        Returns: Employees
        """
        queryset = Employee.objects.all()

        filters = {}

        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "birth_date": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Employee Date of birth"
                ),
                "first_name": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Employee First name"
                ),
                "last_name": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Employee last name"
                ),
                "gender": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Employee gender (M/F)"
                ),
                "hire_date": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Employee hire date"
                ),
            }
        )
    )
    def post(self, request, format=None):
        """
        Used to create a new Employee

        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
