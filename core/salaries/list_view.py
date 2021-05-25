from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from core.db_models.salaries import Salaries
from core.salaries.serializers import SalariesSerializer


class SalariesListView(APIView):
    """

    """
    serializer_class = SalariesSerializer

    def get(self, request, format=None):
        """

        """

        queryset = Salaries.objects.prefetch_related(
            'emp_no'
        ).all().order_by("emp_no")[:800]  # TODO figure out how to display all
        # salaries
        # without
        # affecting performance

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "emp_no": openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description="Employee number"
                ),
                "salary": openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description="Employee Salary"
                ),
                "from_date": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Employee Start date"
                ),
                "to_date": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description="Employee end date for this employee/salary"
                ),
            }
        )
    )
    def post(self, request, format=None):
        """
        Create a Salary for an existing employee
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
