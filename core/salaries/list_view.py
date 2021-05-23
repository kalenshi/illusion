from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

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
        ).all()[:800]

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """

        """
        return Response({"message": "Will post nwgotiated salary"},
                        status=status.HTTP_201_CREATED)
