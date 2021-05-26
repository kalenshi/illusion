from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .domain import ProfilesDomain as Domain

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class EmployeeProfileListView(APIView):
    """List of employee profiles"""

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                type=openapi.TYPE_STRING,
                name="from_date",
                description="List all employees who started on this date",
                in_=openapi.IN_QUERY,
                required=False
            )
        ]
    )
    def get(self, request, format=None):
        """
        Filter employee profiles based on a given start date
        """

        filters = {}
        domain = Domain()
        from_date = request.GET.get("from_date", None)

        if from_date:
            filters["from_date"] = from_date

        profiles = domain.get_profiles(**filters)

        return Response(profiles, status=status.HTTP_200_OK)
