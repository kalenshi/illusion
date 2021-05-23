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
        Get the employees Current salary
        """

        try:
            return Salaries.objects.filter(emp_no=pk).latest()
        except Salaries.DoesNotExist:
            raise Http404

    def get(self, request, emp_no):
        """

        """

        salary = self.get_object(emp_no)
        serializer = self.serializer_class(instance=salary)

        return Response(serializer.data, status=status.HTTP_200_OK)
