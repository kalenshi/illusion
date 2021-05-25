from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from core.db_models.salaries import Salaries
from core.salaries.serializers import SalariesSerializer


class SalariesDetailView(APIView):
    """

    """
    serializer_class = SalariesSerializer

    def get_object(self, pk):
        """
        Get the employees salary history
        """

        try:
            return Salaries.objects.filter(emp_no=pk)
        except Salaries.DoesNotExist:
            raise Http404

    def get(self, request, emp_no):
        """
        Retrieve the latest salary details using the employee number
        """

        salaries = self.get_object(emp_no)
        serializer = self.serializer_class(instance=salaries, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
